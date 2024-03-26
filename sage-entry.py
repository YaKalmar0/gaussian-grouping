import subprocess
import shutil
import sys

if "__name__" == "__main__":
    subprocess.call(['conda', 'env', 'create', '-f', 'environment.yml'])
    subprocess.call(['source', 'activate', 'gaussian_grouping2'])   
    print(subprocess.run([sys.executable, "./script/train.sh", "mipnerf/kitchen", "2"]))
    shutil.move('./output', '/opt/ml/output/data')

    