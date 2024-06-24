import matplotlib.pyplot as plt

# Data for the graph
threats = ["Spoofing", "Tampering", "Repudiation", "Information Disclosure", "Denial of Service (DoS)", "Elevation of Privilege"]
risk_levels = [6, 2, 4, 9, 6, 6]

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(threats, risk_levels, marker='o', linestyle='-', color='b', label='Total Risk')

# Add labels to the graph
plt.xlabel('Threat/Vulnerability', fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Risk Level (Likelihood x Impact)', fontweight='bold')
plt.title('Quantitative Cybersecurity Risk Assessment', fontweight='bold')

# Add a legend
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
