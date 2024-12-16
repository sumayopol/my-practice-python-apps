import random

def athletes_list():

    world_class_athletes = [
        "Messi", "Ronaldo", "Neymar", "Mbappe", "Lewandowski", "Benzema", "Modric", "Salah", "Kane", "Haaland",
        "Kante", "Suarez", "Ramos", "Alisson", "Courtois", "Mane", "Firmino", "Griezmann", "Hazard", "Pogba",
        "Sterling", "Aguero", "Silva", "Fernandes", "Debruyne", "Lukaku", "Aubameyang", "Lloris", "Oblak", "Varane",
        "Vidal", "Pique", "Dybala", "Chiellini", "Buffon", "Casemiro", "Neuer", "Gundogan", "Kroos", "Cavani",
        "Mahrez", "Pepe", "Thiago", "Werner", "Gomez", "Jota", "Ziyech", "Foden", "Mertens", "Immobile",
        "Benz", "Felix", "Bale", "Martial", "Mount", "Icardi", "Son", "Rodriguez", "Depay", "Tadic",
        "Sancho", "Zaha", "Werner", "Abraham", "Insigne", "Vardy", "Morata", "Keane", "Mina", "Richarlison",
        "Alli", "Arnautovic", "Higuain", "Giroud", "Pulisic", "Rashford", "James", "Maguire", "Reus", "Hummels",
        "Sane", "Robertson", "Fabinho", "Militao", "Alaba", "Goretzka", "Havertz", "Chiesa", "Torres", "Partey",
        "Dembele", "Vinicius", "Barella", "Locatelli", "DiMaria", "Zielinski", "Correa", "Acuna", "Koulibaly", "Grealish"
    ]
    # Generate a list of 100 random school-related words
    athletes_name = random.choice(world_class_athletes).lower()

    # Print the list
    #return athletes_name
    return athletes_name

athletes_list()

def school_words():

    words = [
        "classroom", "teacher", "student", "homework", "desk", "blackboard", "chalk", "eraser", "notebook",
        "pencil", "marker", "exam", "test", "quiz", "assignment", "grade", "textbook", "library", "cafeteria",
        "gymnasium", "recess", "playground", "principal", "schedule", "subject", "science", "mathematics",
        "history", "geography", "biology", "chemistry", "physics", "literature", "art", "music", "drama",
        "computer", "lab", "project", "group", "friend", "classmate", "teacher's aide", "hallway", "locker",
        "timetable", "lesson", "whiteboard", "curriculum", "study", "discipline", "detention", "school bell",
        "extracurricular", "club", "sport", "uniform", "graduation", "diploma", "college", "university",
        "lecture", "seminar", "professor", "scholarship", "research", "essay", "draft", "presentation",
        "assignment", "deadline", "field trip", "report card", "campus", "assembly", "tutorial", "student council",
        "headmaster", "kindergarten", "preschool", "nursery", "scholar", "mentor", "examiner", "syllabus",
        "chapter", "revision", "practice", "parent-teacher meeting", "resource", "calculator", "stationery",
        "whiteout", "glue", "ruler", "highlighter"
    ]

    # Generate a list of 100 random school-related words
    school_word = random.choice(words).lower

    # Print the list
    return school_word

def names():

    first_names = [
        "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Sophia", "James", "Isabella",
        "William", "Mia", "Benjamin", "Charlotte", "Lucas", "Amelia", "Henry", "Harper", "Alexander", "Evelyn",
        "Michael", "Abigail", "Daniel", "Ella", "Matthew", "Elizabeth", "Ethan", "Sofia", "Jacob", "Avery",
        "Sebastian", "Scarlett", "Jack", "Madison", "Owen", "Layla", "Aiden", "Chloe", "Samuel", "Grace",
        "Joseph", "Ellie", "John", "Nora", "David", "Zoey", "Leo", "Mila", "Wyatt", "Lily"
    ]

    # Generate a list of 100 random school-related words
    random_first_names = random.choice(first_names)

    # Print the list
    print(random_first_names)

    religious_words = [
        "prayer", "faith", "worship", "scripture", "temple", "church", "mosque", "synagogue", "meditation",
        "blessing", "ritual", "sacrament", "bible", "quran", "torah", "psalm", "hymn", "pilgrimage",
        "monastery", "clergy", "saint", "prophet", "disciple", "angel", "spirituality", "redemption",
        "forgiveness", "salvation", "soul", "divine", "eternal", "grace", "piety", "holy", "sacred",
        "altar", "reverence", "ceremony", "creed", "doctrine", "heaven", "hell", "paradise", "karma",
        "nirvana", "enlightenment", "idolatry", "priest", "pastor", "rabbi", "imam", "guru", "shrine",
        "fasting", "sacrifice", "martyr", "gospel", "apostle", "reincarnation", "creation", "covenant",
        "tabernacle", "chapel", "rosary", "baptism", "confirmation", "ordination", "vow", "holiness",
        "sanctuary", "cathedral", "abbey", "meditation", "congregation", "fellowship", "charity",
        "devotion", "miracle", "penance", "absolution", "evangelism", "missionary", "praise", "offering",
        "anointing", "liturgy", "atonement", "repentance", "grace", "divinity", "providence", "omnipotent",
        "omniscient", "transcendence", "pilgrim", "priesthood"
    ]
    # Generate a list of 100 random religious-related words
    random_religious_words = random.choice(religious_words).lower()

    # Print the list
    return random_religious_words



    # Lists of sample countries and presidents (fictional or real-world)
def countries():

    country = [
        "United States", "France", "Brazil", "India", "China", "Russia", "South Africa", "Canada",
        "Germany", "Australia", "Mexico", "Italy", "Japan", "South Korea", "Argentina", "Spain",
        "Nigeria", "Egypt", "Turkey", "Indonesia"
    ]

    # Generate a list of 100 random religious-related words
    random_country = random.choice(country).lower()

    # Print the list
    return random_country

def presidents():

    president = [
        "Joe Biden", "Emmanuel Macron", "Luiz Inácio Lula da Silva", "Droupadi Murmu", "Xi Jinping",
        "Vladimir Putin", "Cyril Ramaphosa", "Justin Trudeau", "Frank-Walter Steinmeier", "David Hurley",
        "Andrés Manuel López Obrador", "Sergio Mattarella", "Fumio Kishida", "Yoon Suk-yeol",
        "Alberto Fernández", "Felipe VI", "Bola Ahmed Tinubu", "Abdel Fattah el-Sisi", "Recep Tayyip Erdoğan",
        "Joko Widodo"
    ]

    # Create a dictionary by randomly pairing countries with presidents
    random_president = random.choice(president).lower()

    # Print the dictionary
    print(random_president)
