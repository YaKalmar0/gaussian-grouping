import subprocess
import shutil
import os
from pathlib import Path

if __name__ == "__main__":
    print('Extracting train output...')
    outp_dir = os.environ["SM_CHANNEL_OUTP"]
    print('Data dir:', os.listdir(outp_dir))
    os.mkdir('./output')
    shutil.move(os.path.join(outp_dir, 'lerf'), './output')
    print("Localdir:", os.listdir('./'))
    print("Datadir:", os.listdir('./output'))


    print(subprocess.run(["python", "train.py", "-s", os.environ["SM_CHANNEL_TRAIN"], "-r", "1", "-m", "output/lerf/ramen", "--config_file config/gaussian_dataset/train.json", "--train_split"]))
    shutil.move('./output', '/opt/ml/output/data')
