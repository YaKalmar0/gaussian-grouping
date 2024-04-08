import subprocess
import shutil
import tarfile
import os
from pathlib import Path

if __name__ == "__main__":
    print('Extracting train output...')
    outp_dir = os.environ["SM_CHANNEL_OUTP"]
    print('Data dir:', os.listdir(outp_dir))
    os.mkdir('./output')
    with tarfile.open(Path(outp_dir) / 'output.tar.gz') as tar:
        tar.extractall('./output')
    print("Localdir:", os.listdir('./'))
    print("Datadir:", os.listdir('./output'))

    # os.mkdir('./data')
    # data_dir = os.environ["SM_CHANNEL_TRAIN"]
    # shutil.move(f'{data_dir}/lerf', './data')
    # print("Datadir:", os.listdir('./data'))

    print(subprocess.run(["python", "render.py", "-m", "output/lerf/ramen", "--num_classes", "256", "--images", "images"]))
    shutil.move('./output', '/opt/ml/output/data')
    

    