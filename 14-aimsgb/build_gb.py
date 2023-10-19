from aimsgb import Grain, GrainBoundary

s_input = Grain.from_file("POSCAR_W")
# gb = GrainBoundary([1, 1, 1], 3, [2, 1, 1], s_input)
gb = GrainBoundary([0, 0, 1], 5, [1, 2, 0], s_input)
structure = Grain.stack_grains(gb.grain_a, gb.grain_b, direction=gb.direction)

print(structure)
structure.to("POSCAR_W_gb")
