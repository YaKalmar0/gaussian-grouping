import subprocess
import shutil
import sys
import os

if __name__ == "__main__":
    print('Configuring Conda environment...')
    subprocess.call(['conda', 'env', 'create', '-f', 'environment.yml'])
    subprocess.call(['source', 'activate', 'gaussian_grouping2'])
    print('Conda environment successfully configured')
    
    print('Moving dataset...')
    data_dir = os.environ["SM_CHANNEL_TRAIN"]
    os.mkdir('./data')
    shutil.move(data_dir, './data')
    print('Dataset successfully moved')

    print(subprocess.run([sys.executable, "./script/train.sh", "mipnerf/kitchen", "2"]))
    shutil.move('./output', '/opt/ml/output/data')
    

    