# Code Institute

Welcome kevald1963,

We have preinstalled all of the tools you need to get started.

>>>

Well not exactly, because the 'dnspython' library wasn't installed. You have to do this manually.
If you forget to do it, you can still connect to MongoDB but can't do any CRUD oerations. It was 
installed once as per the instructions in the CI course video but, unfortunately, Gitpod seems to
'lose' the installed library sometimes, so has to be re-installed. Not sure why this happens. 
Doesn't appear to be related to stopping the Gitpod project. Went round in circles trying to find 
out what had went wrong! 

On AWS Cloud 9 and similar platforms use: 'sudo pip3 install dnspython'.

On Gitpod, sudo is not allowed so just use: 'pip3 install dnspython'.

>>>