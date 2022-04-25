## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Chongrui1/Assignment1.github.io/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

### Header 1
mode.py : This file is the main runtime file for this program,the content of the code includes the implementation of various functions, for instance,loading of coordinate systems and reading of background image.There is also code about running front-end pages directly.There are also calls to various functions in other documents, such as movement, eating, interaction between agent points, etc.
Part of main function code:
for i in range(num_of_agents): 
        print(agents[i])
        agents[i].move(d)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
    for j in range(num_of_cats):
        cats[j].move(distance)
        print(cats[j])   
            
      
    
    # animation = matplotlib.animation.FuncAnimation(fig, update, interval=1)
    for j in range(num_of_cats):
        matplotlib.pyplot.scatter(cats[j].x,cats[j].y, color = cats[j].color)
    


### Header 2

agentframework.py: This file contains the initialisation of the various ‘rat’ parameters.Various other functions,such as eat, move_coordinate, and most importantly, the interact with each agent points, etc.

### Header 3

catsframework.py: This file contains the initialisation of the various ‘cats’ parameters.the functions are similar to the ‘agentframework’.
How to run it?

Open the model.py document, run it, in the dialogue of the “Model of cat catching rates”, click on the “Model”,then click on the the “Run Programme”, this programme will run successfully.



**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Chongrui1/Assignment1.github.io/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
