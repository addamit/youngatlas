`youngatlas` is a jupyter notebook python package extension. 


# The Story #


These days you call your friends to keep in touch. One time, I was catching up with an old colleague of mine and towards the tail end of our conversation we started talking about about how all of us have to do our part in dealing with this global COVID situation. He mentioned how his family built a COVID tracker dashboard. I can totally imagine how something like this could be useful to officials, organizations and communities. It was a great way to contribute.

I moved on to my daily/weekly chores like I usually do, feeling inspired.  Except this time there was this constant voice in my head that kept talking to me "you need to do a project and finish it and I will not leave you until you do" 

But I wasn't sure what to do. 

As part of my work, I usually spend hours on jupyter notebooks. 
A couple of weeks ago, almost towards the end of the day, exhausted, I was squinting hard on a piece of code on a notebook cell trying to make sense of it. There was too much distraction with my kids watching TV in the other room.
I couldn't focus on what I was doing and decided to take a break and join the kids. They were watching  `Avatar the last airbender` on Netflix. 

After watching the show for some time, I realized there was such a great deal of wisdom in the lines spoken by the characters and so much of their struggle is relevant to our current stressful times due to the pandemic.

After my break, I went back to my desk glaring at the same piece of code, and it seemed just obvious this time what the bug was. 
Right then, the idea for a notebook extension was born. How about an extension that plays some of the best quotes from the shows you enjoyed watching.
You can listen to just when you want to take a break or while you are having a down moment to remind you on things that truly matter. 

Or when a long running task on a cell such as training your neural net or a data transformation job is taking too long to finish, what if Iroh of Avatar can notify you when the long running task got completed with a pretty good advice and a reminder on enjoying and taking a tea break. 

So as a working prototype, I have quickly put together a notebook extension with just a few sound clips from some of my favourite characters from Avatar. Currently the extension has quotes from antihero zuko and my personal favourite zuko's uncle Iroh. And I have added a few more.


## How to Install ##


You can directly install after cloning from the source like so:
```
pip install git+https://github.com/addamit/youngatlas.git
```

Or git clone the repo first and install
```
git clone https://github.com/addamit/youngatlas.git
```


now cd to the cloned repo folder and run 
```
pip install setup.py
```


## How to run ##


After you have successfully installed the extension, you can run the extension in any jupyter notebook by typing the magic %youngatlas in any code cell, just before you start typing any code. 

See sample notebook in the example folder

Once the cell finishes execution, you will be showered with deep meaning wisdom audio clip (about 10-20 seconds) that might make a connection with you. Be sure to keep your computer/laptop sound button unmuted so you can hear the clip.


 # Contributing #

Send pull requests, open feature requests or DM me on twitter `@addamit` for any collaboration.

 
To build the package `python setup.py sdist bdist_wheel`

To install 
 `pip install --no-index --find-link=dist/ youngatlas==0.1`


For local development of packages:
pip install -e .

For manually enabling the extension,
To ensure the ipython extension is automatically defined in the IPython profile and loaded automatically when a notebook is launched, you can add it to the IPython profile config script. 

Open file `~/.ipython/profile_default/ipython_config.py` and add the name `youngatlas` in `c.InteractiveShellApp.extensions list`  

Here is a sample content for `~/.ipython/profile_default/ipython_config.py`

```
c.InteractiveShellApp.extensions = [
    'youngatlas',
]
```

And for the notebook extension, 
~/.jupyter/jupyter_notebook_config.json
{
  "NotebookApp": {
    "nbserver_extensions": {
      "yaserver": true
    }
  }
}
```

# Changes #
For changes, see the [change log](CHANGELOG.rst)