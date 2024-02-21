Here is a brief description of the problems:
1- During the execution of index.sh, we come across two clone commands that are not executed because their destination URL is not a repository but It is the absolute file. I think one for Yuna's main model and another for Vision.
 Anyway, this is the way that will probably solve the problems:

First do not attempt to run ( or start ) Yuna till these steps be done!

1- After you have installed the required items through options 2 and 3 on the index.sh page, do this:
 Close the index.sh page using number 5 or 6 ( I'm not sure for now!)
 Navigate terminal to the root directory of the project, which is the folder named ' yuna-ai ' .
 Run this command , carefully:

*        $ mkdir ./lib/models/yuna/

 After that, you can do one of two things below, It depends on which you feel comfortable with:

Way_Number_1:

  a) Run the 'Python Command Line' in your terminal with its Environment Variable's name which could be one of ( python /or/ python3 /or/ python311 /or/ py ).
  
  b) Try running these lines in your  'Python Command Line Environment ' : 

*        >>> import urllib
 
*        >>> url = "https://huggingface.co/TheBloke/Pygmalion-2-7B-GGUF/resolve/main/pygmalion-2-7b.Q5_K_M.gguf";
*        >>> filename = "/content/yuna-ai/lib/models/yuna/yuna-ai-2-7b-role-play.gguf");

*        >>> try: urllib.URLopener().retrieve(url, filename)
         ......  except: urllib.request.urlretrieve(url, filename)

AND WAIT TILL IT DONE!

  c) You can exit 'Python Command Line' with pass the 'exit()' syntax to it.

Way_Number_2:

  a) simply create a temp.py file using txt editor app from your OS and copy these lines:

import urllib
url = "https://huggingface.co/TheBloke/Pygmalion-2-7B-GGUF/resolve/main/pygmalion-2-7b.Q5_K_M.gguf";
filename = "/content/yuna-ai/lib/models/yuna/yuna-ai-2-7b-role-play.gguf");
try: urllib.URLopener().retrieve(url, filename)
except: urllib.request.urlretrieve(url, filename)

  b) then open a terminal and try to execute the temp.py file using your python's Environment Variable's name which could be one of ( python /or/ python3 /or/ python311 /or/ py ) along with the path of our temp.py file.

*       $ python3  path/to/your/temp.py

__________________________________________________________-

2- there is another model which you can do the exact same thing to we just did, with these changes:

( IN THE mkdir PART )::  
                                       first navigate terminal to the root of yuna project witch is 'yuna-ai folder'
*                                     $ mkdir ./lib/models/agi/art/

( IN THE python PART )::

*                                       >>> url = "https://huggingface.co/yukiarimo/anyloli/resolve/main/any_loli.safetensors";
*                                       >>> filename = "/content/yuna-ai/lib/models/agi/art/any_loli.safetensors"

done:)
______________________________________________________________

3- There are some forgotten dependencies, too:

     whisper
     pydub


