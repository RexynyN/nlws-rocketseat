from os import system

pop = [ 
    "https://github.com/rocketseat-education/nlw-journey-html-css-js.git",
    "https://github.com/rocketseat-education/nlw-journey-c-sharp.git",
    "https://github.com/rocketseat-education/nlw-journey-nodejs.git",
    "https://github.com/rocketseat-education/nlw-journey-ia.git",
    "https://github.com/rocketseat-education/nlw-journey-devops.git",
    "https://github.com/rocketseat-education/nlw-journey-java.git",
    "https://github.com/rocketseat-education/nlw-journey-python.git",
    "https://github.com/rocketseat-education/nlw-journey-react.git",
    "https://github.com/rocketseat-education/nlw-journey-react-native.git",
    "https://github.com/rocketseat-education/nlw-journey-go.git",
]

for link in pop: 
    system(f"git clone {link}")