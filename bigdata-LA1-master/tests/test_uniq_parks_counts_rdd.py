import subprocess

def test_uniq_parks_count_rdd():
    command="python ./answers/uniq_parks_counts_rdd.py ./data/frenepublicinjection2016.csv"
    process = subprocess.Popen(command, shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    code=process.wait()
    assert(not code), "Command failed"
    
    assert(process.stdout.read().decode("utf-8")==open("tests/list_parks_count.txt","r").read())
