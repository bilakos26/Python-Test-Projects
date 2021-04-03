from tqdm import tqdm, trange
from time import sleep

with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\test.txt', 'r') as read_f:
    l = read_f.readlines() #Reading all the lines of the file instantly and importing them to a LIST
    with tqdm(total=len(l)) as tl:
        for a in l:
            a = a.rstrip('\n')
            with open(r'C:\Users\bilakos\Desktop\PYTHON_PROJECTS\test1.txt', 'a') as test_f:
                test_f.write(a + '\n')
            tl.set_description(f'Saving {a}') #or tl.set_description('Saving %s'% a) --> It's the same
            if len(l) >= 100:
                tl.update(int(len(l)/100))
                sleep(0.01)
            else: #It works
                tl.update(int(100/len(l))) 
                sleep(1)
        tl.set_description('DONE')
 


#with open('test.txt', 'a') as test_f:
#    a = ['test1', 'test2', 'test3', 'test4', 'test5']
#    with tqdm(total=100, desc="SAVING STATUS") as tl:
#        for i in a:
#            test_f.write(i + '\n')
#            tl.update(int(100/len(a)))

#pbar = tqdm(["a", "b", "c", "d"])
#for char in pbar:
#    sleep(0.25)
#    pbar.set_description("Processing %s" % char)