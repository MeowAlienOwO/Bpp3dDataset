
# python -m bpp3d_dataset.main generate 1d uniform -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "Uniform-1D.json"
# python -m bpp3d_dataset.main generate 1d normal -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "Normal-1D.json"
# python -m bpp3d_dataset.main generate 1d set3 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "Discrete-1D.json"
    # -i 10  -i 15   -i 20  -i 25   -i 30   -i 35   -i 40   -i 45   -i 50   -i 55 \
    # -p 0.2 -p 0.05 -p 0.1 -p 0.12 -p 0.08 -p 0.05 -p 0.03 -p 0.01 -p 0.18 -p 0.18
    


# python -m bpp3d_dataset.main generate 1d uniform -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "UniformLong-1D.json"
# python -m bpp3d_dataset.main generate 1d normal -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "NormalLong-1D.json"
# python -m bpp3d_dataset.main generate 1d set3 -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "DiscreteLong-1D.json"

# python -m bpp3d_dataset.main generate 1d uniform --ir 1 --ir 100 -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "UniformIntensive-1D.json"

# python -m bpp3d_dataset.main generate 1d or-gym-lw0 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymLW0-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-pp0 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymPP0-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-bw0 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymBW0-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-lw1 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymLW1-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-pp1 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymPP1-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-bw1 -C 9 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymBW1-1D.json"

# python -m bpp3d_dataset.main generate 1d or-gym-lw0 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymLW0C100-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-pp0 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymPP0C100-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-bw0 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymBW0C100-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-lw1 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymLW1C100-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-pp1 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymPP1C100-1D.json"
# python -m bpp3d_dataset.main generate 1d or-gym-bw1 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "OrGymBW1C100-1D.json"

# python -m bpp3d_dataset.main generate periodic1d uniform normal -C 100 -N 3000 -S 300 -I 100 -d bpp3d_dataset/data -f "Set1Set2-1D.json"
# python -m bpp3d_dataset.main generate periodic1d uniform set3 -C 100 -N 3000 -S 300 -I 100 -d bpp3d_dataset/data -f "Set1Set3-1D.json"
# python -m bpp3d_dataset.main generate periodic1d uniform normal set3 -C 100 -N 3000 -S 300 -I 100 -d bpp3d_dataset/data -f "Set1Set2Set3-1D.json"



python -m bpp3d_dataset.main generate 1d uniform --ir 1 --ir 100 -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "UniformIntensive-1D.json"
python -m bpp3d_dataset.main generate 1d normal --ir 1 --ir 100 -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "NormalIntensive-1D.json"
python -m bpp3d_dataset.main generate 1d poisson --ir 1 --ir 100 -C 100 -N 3000 -I 100 -d bpp3d_dataset/data -f "PoissonIntensive-1D.json"

python -m bpp3d_dataset.main generate 1d uniform --ir 1 --ir 100 --is 20 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "UniformCoarse-1D.json"
python -m bpp3d_dataset.main generate 1d uniform --ir 5 --ir 55 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "UniformIntensive2-1D.json"
python -m bpp3d_dataset.main generate 1d uniform --ir 5 --ir 25 --is 5 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "UniformSmallItem-1D.json"
python -m bpp3d_dataset.main generate 1d uniform --ir 15 --ir 35 --is 5 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "UniformMiddleItem-1D.json"
python -m bpp3d_dataset.main generate 1d uniform --ir 35 --ir 55 --is 5 -C 100 -N 1000 -I 100 -d bpp3d_dataset/data -f "UniformLargeItem-1D.json"
