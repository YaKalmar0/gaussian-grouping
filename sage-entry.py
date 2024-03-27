import subprocess
import shutil
import sys
import os

if __name__ == "__main__":
    print('Configuring Conda environment...')
    # subprocess.call(['conda', 'create', '-n' 'gaussian_grouping', "python=3.8", '-y'])
    # subprocess.call(['conda', 'init', 'bash'])
    # subprocess.call(['conda', 'activate', 'gaussian_grouping'])
    subprocess.call(['python', '-m', 'pip', 'install', '-r', 'reqs.txt'])
    print('Conda environment successfully configured')
    
    print('Moving dataset...')
    data_dir = os.environ["SM_CHANNEL_TRAIN"]
    os.mkdir('./data')
    print("Datadir:", os.listdir(data_dir))
    shutil.move(f'{data_dir}', './data')
    print("Datadir:", os.listdir('./data'))
    print('Dataset successfully moved')

    print(subprocess.run(["bash", "./script/train.sh", "train/mipnerf/kitchen", "2"]))
    shutil.move('./output', '/opt/ml/output/data')
    

    