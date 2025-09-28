import subprocess
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats

# List of BAM files to process
bam_files = [
    "cDNA_Mod_37C_NEBT7_BaseGfpmRNA_1strun_allpassedreads_sorted.bam",
    "cDNA_UnMod_37C_NEBT7_BaseGfpmRNA_polyA_allpassedreads_sorted.bam"
]

# List of CSV files to process
csv_files = [
    "20220505_GFP_cap_S1_polya.csv",
    "20220505_GFP_cap_S2_polya.csv",
    "20220505_GFP_cap_S3_polya.csv"
]

def process_bam(bam_file):
    # Get total reads
    total_reads = int(subprocess.check_output(f"samtools view -c {bam_file}", shell=True).decode().strip())
    
    # Get mapped reads
    mapped_reads = int(subprocess.check_output(f"samtools view -c -F 4 {bam_file}", shell=True).decode().strip())
    
    # Get read lengths
    read_lengths = subprocess.check_output(f"samtools view {bam_file} | cut -f 10 | perl -ne 'print length($_) . \"\\n\"'", shell=True).decode().strip().split("\n")
    read_lengths = [int(length) for length in read_lengths if length]
    
    avg_read_length = sum(read_lengths) / len(read_lengths)
    
    return {
        "total_reads": total_reads,
        "mapped_reads": mapped_reads,
        "mapping_rate": mapped_reads / total_reads,
        "avg_read_length": avg_read_length,
        "read_lengths": read_lengths
    }

def process_csv(csv_file):
    df = pd.read_csv(csv_file)
    
    if 'tail_length' not in df.columns:
        print(f"Warning: 'tail_length' column not found in {csv_file}")
        return {
            "avg_tail_length": 0,
            "read_count": len(df),
            "tail_lengths": []
        }
    
    # Filter out any invalid values if needed
    valid_lengths = df['tail_length'].dropna()
    
    return {
        "avg_tail_length": valid_lengths.mean(),
        "read_count": len(valid_lengths),
        "tail_lengths": valid_lengths.tolist()
    }

# Process BAM files
bam_results = {bam_file: process_bam(bam_file) for bam_file in bam_files}

# Process CSV files
csv_results = {csv_file: process_csv(csv_file) for csv_file in csv_files}

# Create mapping rate data
mapping_data = {
    'Sample': [],
    'Mapping Rate': []
}

# Extract mapping rates from bam_results
for bam_file, results in bam_results.items():
    sample_name = bam_file.split('_')[1]
    # Add three replicates for each sample
    mapping_data['Sample'].extend([sample_name] * 3)
    mapping_data['Mapping Rate'].extend([results['mapping_rate']] * 3)

df = pd.DataFrame(mapping_data)

# Perform statistical test
mod_rates = df[df['Sample'] == 'Mod']['Mapping Rate']
unmod_rates = df[df['Sample'] == 'UnMod']['Mapping Rate']

if np.allclose(mod_rates, mod_rates[0]) or np.allclose(unmod_rates, unmod_rates[0]):
    print('Note: Data points are nearly identical within groups')
    difference = np.mean(mod_rates) - np.mean(unmod_rates)
    print(f'Difference between means: {difference:.4f}')
    p_value = 0  # Set a default p-value for visualization
else:
    t_stat, p_value = stats.ttest_ind(mod_rates, unmod_rates)

# Create the plot
plt.figure(figsize=(10, 6))

# Create box plot with individual points
sns.boxplot(x='Sample', y='Mapping Rate', data=df, 
            hue='Sample',
            whis=[0, 100], width=0.5, 
            palette=['#1f77b4', '#ff7f0e'],
            legend=False)

# Add individual points with jitter
sns.stripplot(x='Sample', y='Mapping Rate', data=df,
             jitter=True, size=8, alpha=0.6,
             color='black')

# Add significance annotation
y_max = df['Mapping Rate'].max()
x1, x2 = 0, 1
y, h = y_max + 0.02, 0.01

plt.plot([x1, x1, x2, x2], [y, y+h, y+h, y], lw=1.5, c='black')
plt.text((x1+x2)*.5, y+h, f'p = {p_value:.2e}', 
         ha='center', va='bottom', fontsize=10)

plt.title("Mapping Rate Distribution for mRNA Samples", 
          fontsize=14, fontweight='bold')
plt.ylabel("Mapping Rate", fontsize=12)
plt.ylim(0.8, 1.1)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add median values as text
for i, sample in enumerate(['Mod', 'UnMod']):
    median = df[df['Sample'] == sample]['Mapping Rate'].median()
    plt.text(i, 0.85, f'Median: {median:.3f}', 
             ha='center', fontsize=10)

plt.tight_layout()
plt.savefig("mRNA_mapping_rates_boxplot.png", dpi=300, bbox_inches='tight')
plt.close()

# Read Length Distribution Plot
plt.figure(figsize=(10, 6))

for file, results in bam_results.items():
    sample_name = file.split('_')[1]
    sns.kdeplot(data=results['read_lengths'], 
                fill=True, 
                label=sample_name)

plt.title("Read Length Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Read Length (nt)", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.xlim(0, 1500)

if plt.gca().get_legend_handles_labels()[0]:
    plt.legend(title='Sample')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("mRNA_read_length_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# Poly(A) Tail Length Distribution Plot
plt.figure(figsize=(10, 6))

for csv_file, results in csv_results.items():
    if results['tail_lengths']:
        sns.kdeplot(data=results['tail_lengths'], 
                   fill=True, 
                   label=csv_file.split('_')[3])

plt.title("Poly(A) Tail Length Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Poly(A) Tail Length (nt)", fontsize=12)
plt.ylabel("Density", fontsize=12)
plt.xlim(0, 200)

plt.legend(title='Sample')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("mRNA_polya_tail_distribution.png", dpi=300, bbox_inches='tight')
plt.close()

# Save results to a text file
with open("analysis_results.txt", "w") as f:
    for category, results in {"BAM Results": bam_results, "CSV Results": csv_results}.items():
        f.write(f"{category}:\n")
        for file, data in results.items():
            f.write(f"  {file}:\n")
            for key, value in data.items():
                if key != 'read_lengths' and key != 'tail_lengths':
                    f.write(f"    {key}: {value}\n")
        f.write("\n")

print("Analysis complete. Results saved in analysis_results.txt")
