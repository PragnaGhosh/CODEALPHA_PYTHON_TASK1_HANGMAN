import random
import hangman_stages
word_list= [
    "hangman", "python", "programming", "game", "javascript", "web",
    "computer", "science", "algorithm", "database", "network", "security",
    "software", "development", "application", "interface", "backend", "frontend",
    "html", "css", "javascript", "jquery", "react", "angular", "vue", "node",
    "server", "client", "cloud", "storage", "authentication", "authorization",
    "encryption", "decryption", "machine", "learning", "artificial", "intelligence",
    "neural", "network", "deep", "learning", "data", "analysis", "visualization",
    "algorithm", "structure", "language", "compiler", "interpreter", "operating",
    "system", "kernel", "virtualization", "container", "docker", "kubernetes",
    "microservice", "architecture", "scalability", "performance", "testing", "debugging",
    "version", "control", "git", "repository", "branch", "merge", "conflict",
    "documentation", "agile", "scrum", "kanban", "waterfall", "methodology", "framework",
    "library", "package", "module", "dependency", "integration", "deployment", "continuous",
    "delivery", "automation", "monitoring", "logging", "analytics", "metrics", "dashboard",
    "user", "experience", "interface", "design", "responsive", "mobile", "optimization",
    "security", "vulnerability", "penetration", "testing", "patch", "update", "release",
    "patch", "version", "upgrade", "downgrade", "rollback", "backup", "restore",
    "performance", "optimization", "benchmark", "load", "testing", "stress", "test",
    "error", "handling", "exception", "try", "catch", "finally", "debugging",
    "log", "file", "configuration", "parameter", "setting", "environment", "variable",
    "dependency", "injection", "singleton", "factory", "method", "class", "object",
    "inheritance", "polymorphism", "encapsulation", "abstraction", "interface", "protocol"
]

live=6
chosen_word=random.choice(word_list)
print(chosen_word)
display=[]
for i in chosen_word:
    display+="_"
print(display)
game_over=False
while not game_over:
    guess=input("Guess a letter: ").lower()
    print(guess)
    for position in range(len(chosen_word)):
        if chosen_word[position]==guess:
            display[position]=guess
    print(display)
    if guess not in chosen_word:
        print(guess+" is not present in the world")
        live-=1
        if live==0:
            game_over=True
            print("You Lose!")
    else:
        print(guess+" is present in the world")
    if '_' not in display:
        game_over=True
        print("You Win!")
    print(hangman_stages.stages[live])
      
            
