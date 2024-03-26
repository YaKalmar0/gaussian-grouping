import subprocess
import shutil
import sys
import os

if "__name__" == "__main__":
    subprocess.call(['conda', 'env', 'create', '-f', 'environment.yml'])
    subprocess.call(['source', 'activate', 'gaussian_grouping2'])
    data_dir = os.environ["SM_CHANNEL_TRAIN"]
    os.mkdir('./data')
    shutil.move(data_dir, './data')


    print(subprocess.run([sys.executable, "./script/train.sh", "mipnerf/kitchen", "2"]))
    shutil.move('./output', '/opt/ml/output/data')
    

    