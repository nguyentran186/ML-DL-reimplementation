import torch

# Check if PyTorch is installed
print("PyTorch version:", torch.__version__)

# Check if CUDA is available (for GPU installations)
print("CUDA available:", torch.cuda.is_available())

# Create a tensor and perform a simple operation
x = torch.rand(5, 3)
print("Random tensor:\n", x)

y = torch.ones_like(x)
print("Tensor of ones:\n", y)

z = x + y
print("Result of tensor addition:\n", z)
