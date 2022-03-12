import matplotlib.pyplot as plt

import utils.mpl_styles as mpl_styles

mpl_styles.set_default_styles()

# Plot the model accuracy over the epochs.
markers = ['-o', '--^']
x = [[0, 1, 2, 3, 4, 5, 6],
     [0, 1, 2, 3, 4, 5, 6]]
y = [[0.0, 0.43, 0.69, 0.81, 0.89, 0.92, 0.92],
     [0.0, 0.31, 0.52, 0.71, 0.8, 0.88, 0.92]]

for idx in range(len(x)):
  plt.plot(x[idx], y[idx], markers[idx])

# plt.annotate('80% Accuracy')

plt.legend(['Sample Efficient Model', 'Baseline Model'], loc='lower right')

plt.title('Sample Efficiency')
plt.xlabel('Training Epochs')
plt.ylabel('Accuracy')
plt.show()