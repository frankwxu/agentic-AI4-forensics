# MNIST Data Note

The notebook in this supplement downloads MNIST through `torchvision.datasets.MNIST` and stores the files in this directory. The downloaded dataset is ignored by Git; this note is the only dataset file committed to the repository.

## Source and Attribution

- Dataset: MNIST database of handwritten digits
- Creators: Yann LeCun, Corinna Cortes, and Christopher J. C. Burges
- Dataset page: <https://yann.lecun.com/exdb/mnist/>
- Torchvision loader: <https://pytorch.org/vision/stable/generated/torchvision.datasets.MNIST.html>

MNIST contains grayscale images of handwritten digits at `28 × 28` pixels. The notebook uses only digit `3` and digit `8`. It selects 1,000 examples of each class from the official training split and 200 examples of each class from the official test split with a fixed random seed.

Torchvision downloads MNIST from one of its configured mirrors. Users who redistribute the dataset should consult the dataset page for its terms and citation guidance.
