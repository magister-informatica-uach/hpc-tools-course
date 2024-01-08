import sys
from fractal import make_fractal

sys.activate_stack_trampoline("perf")
make_fractal(50)
sys.deactivate_stack_trampoline()
