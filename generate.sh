
python -m bpp3d_dataset.main generate 1d uniform -C 100 -N 1000 -I 10 -d bpp3d_dataset/data
python -m bpp3d_dataset.main generate 1d normal -C 100 -N 1000 -I 10 -d bpp3d_dataset/data
python -m bpp3d_dataset.main generate 1d discrete -C 100 -N 1000 -I 10 -d bpp3d_dataset/data \
    -i 10  -i 15   -i 20  -i 25   -i 30   -i 35   -i 40   -i 45   -i 50   -i 55 \
    -p 0.2 -p 0.05 -p 0.1 -p 0.12 -p 0.08 -p 0.05 -p 0.03 -p 0.01 -p 0.18 -p 0.18

