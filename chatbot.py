import random


class AetherBot:

    def __init__(self):

         self.greetings = [

    "Hello! I'm Aether AI.",
    "Welcome back, explorer.",
    "Greetings. Ready to learn something new?",
    "Hello. Ask me anything about technology or science.",
    "Hi there. Let's build the future together."
]

         self.quizzes = {

    "python": [

        "Q1: Which keyword defines a function?\nA) func\nB) define\nC) def\nD) function\n\nAnswer: C",

        "Q2: Which data type stores text?\nA) int\nB) str\nC) float\nD) bool\n\nAnswer: B",

        "Q3: Python is a?\nA) Compiler\nB) Language\nC) Database\nD) OS\n\nAnswer: B"
    ],

    "ai": [

        "Q1: What does AI stand for?\nA) Artificial Intelligence\nB) Automated Interface\nC) Advanced Internet\nD) Algorithmic Input\n\nAnswer: A",

        "Q2: Machine Learning is a subset of?\nA) Physics\nB) Chemistry\nC) AI\nD) Networking\n\nAnswer: C"
    ],

    "physics": [

        "Q1: Newton's Second Law?\nAnswer: F = ma",

        "Q2: SI Unit of Force?\nAnswer: Newton",

        "Q3: Speed of Light?\nAnswer: 3 × 10⁸ m/s"
    ]
         }
         self.formulas = {

    "lift":
    "Lift Equation: L = 1/2 × ρ × V² × S × CL",

    "drag":
    "Drag Equation: D = 1/2 × ρ × V² × S × CD",

    "newton":
    "Force Equation: F = ma",

    "kinetic energy":
    "KE = 1/2 mv²",

    "potential energy":
    "PE = mgh",

    "bernoulli":
    "P + 1/2ρV² + ρgh = Constant"
}

         self.study_topics = {

    "bernoulli theorem":
    "Bernoulli's theorem states that an increase in fluid velocity causes a decrease in pressure.",

    "mach number":
    "Mach Number = Object Speed / Speed of Sound",

    "shock wave":
    "Shock waves occur when an object travels faster than the speed of sound.",

    "airfoil":
    "An airfoil is a shape designed to generate lift.",

    "reynolds number":
    "Re = ρVD / μ"
}
        
       

         self.responses = {

            # Greetings
            "hello": [
                "Hello! Welcome to Aether AI.",
                "Greetings, future innovator.",
                "Hi there! How can I help you today?",
                "Welcome back. Ready to explore technology?",
                "Hello! Let's learn something amazing today."
            ],

            "hi": [
                "Hello!",
                "Hi, how are you doing?",
                "Greetings from Aether AI.",
                "Nice to meet you.",
                "Ready to learn something new?"
            ],

            # AI
            "ai": [
                "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",
                "AI powers virtual assistants, recommendation systems, robotics and autonomous vehicles.",
                "Machine Learning and Deep Learning are major branches of AI.",
                "AI is transforming healthcare, education, aerospace and cybersecurity.",
                "The future of AI involves human-AI collaboration."
            ],

            "machine learning": [
                "Machine Learning allows systems to learn from data without explicit programming.",
                "Supervised learning uses labeled data.",
                "Unsupervised learning finds hidden patterns.",
                "Reinforcement learning learns through rewards and penalties.",
                "ML is used in image recognition, NLP and prediction systems."
            ],

            # Programming
            "programming": [
                "Programming is the art of instructing computers to solve problems.",
                "Consistent practice improves coding skills.",
                "Start with logic before focusing on syntax.",
                "Every great software engineer started as a beginner.",
                "Build projects to learn programming effectively."
            ],

            "python": [
                "Python is widely used in AI, automation and data science.",
                "Python is beginner friendly and powerful.",
                "Python supports object-oriented and functional programming.",
                "Flask and Django are popular Python frameworks.",
                "Python is one of the most in-demand languages."
            ],

            "java": [
                "Java powers Android apps and enterprise systems.",
                "Java follows the Write Once Run Anywhere principle.",
                "Java uses JVM for platform independence.",
                "Object-oriented programming is a core Java concept.",
                "Java remains one of the most popular languages."
            ],

            "c programming": [
                "C is a foundational programming language.",
                "Many modern languages were influenced by C.",
                "C provides direct memory access using pointers.",
                "Operating systems are often developed using C.",
                "Learning C strengthens programming fundamentals."
            ],

            # Android
            "android": [
                "Android is the world's most popular mobile operating system.",
                "Android Studio is the official IDE for Android development.",
                "Java and Kotlin are commonly used for Android apps.",
                "Android applications are packaged as APK files.",
                "Android development combines UI design and programming."
            ],

            "android studio": [
                "Android Studio is built on IntelliJ IDEA.",
                "It provides emulators, debugging tools and Gradle support.",
                "XML is commonly used for Android layouts.",
                "Android Studio simplifies app development.",
                "Modern Android apps use AndroidX libraries."
            ],

            # Cybersecurity
            "cybersecurity": [
                "Cybersecurity protects systems, networks and data.",
                "Strong passwords improve security.",
                "Multi-factor authentication adds protection.",
                "Ethical hackers identify vulnerabilities.",
                "Security is everyone's responsibility."
            ],

            "hacking": [
                "Ethical hacking helps improve security.",
                "Always practice hacking legally and responsibly.",
                "Cybersecurity professionals protect digital systems.",
                "Penetration testing identifies weaknesses.",
                "Learning networking is important for cybersecurity."
            ],

            # Robotics
            "robotics": [
                "Robotics combines mechanics, electronics and software.",
                "Robots improve efficiency and precision.",
                "AI enhances robotic decision making.",
                "Industrial robots are widely used in manufacturing.",
                "Future robots will become increasingly autonomous."
            ],

            # Computer Science
            "computer": [
                "A computer processes data into useful information.",
                "Computers consist of hardware and software.",
                "Modern computing powers nearly every industry.",
                "Computers execute instructions through processors.",
                "Computer science drives technological innovation."
            ],

            "cpu": [
                "CPU stands for Central Processing Unit.",
                "The CPU executes program instructions.",
                "Clock speed affects processing performance.",
                "Modern CPUs contain multiple cores.",
                "The CPU is often called the brain of the computer."
            ],

            "gpu": [
                "GPU stands for Graphics Processing Unit.",
                "GPUs accelerate graphics and AI workloads.",
                "Parallel processing is a key GPU strength.",
                "Modern AI training often relies on GPUs.",
                "Gaming and scientific computing benefit from GPUs."
            ],

            # Technology
            "technology": [
                "Technology shapes the future of humanity.",
                "Innovation drives progress.",
                "Emerging technologies create new opportunities.",
                "Technology improves productivity and connectivity.",
                "Continuous learning is essential in technology."
            ],

            "future": [
                "The future will be driven by AI, robotics and automation.",
                "Quantum computing may revolutionize problem solving.",
                "Renewable energy technologies are expanding rapidly.",
                "Space exploration is advancing quickly.",
                "Innovation creates the future."
            ],

            # Mathematics
            "math": [
                "Mathematics is the language of science.",
                "Practice is the key to mastering mathematics.",
                "Calculus is essential in engineering.",
                "Algebra forms the foundation of advanced math.",
                "Mathematics develops analytical thinking."
            ],

            "calculus": [
                "Calculus studies change and motion.",
                "Differentiation measures rates of change.",
                "Integration measures accumulation.",
                "Calculus is vital in physics and engineering.",
                "Newton and Leibniz developed calculus independently."
            ],

            "algebra": [
                "Algebra uses symbols to represent quantities.",
                "Equations express mathematical relationships.",
                "Algebra is fundamental to advanced mathematics.",
                "Variables allow generalized problem solving.",
                "Algebra improves logical reasoning."
            ],

            # Physics
            "physics": [
                "Physics studies matter, energy and motion.",
                "Newton's laws explain classical mechanics.",
                "Physics is fundamental to engineering.",
                "Aerodynamics relies heavily on physics.",
                "Physics helps explain the universe."
            ],

            "newton": [
                "Newton formulated the laws of motion.",
                "Force equals mass multiplied by acceleration.",
                "Newton's work transformed science.",
                "Classical mechanics is based on Newtonian principles.",
                "Newton contributed to calculus and optics."
            ],

            "aerodynamics": [
                "Aerodynamics studies airflow around objects.",
                "Lift and drag are major aerodynamic forces.",
                "Aircraft performance depends on aerodynamic design.",
                "Airfoils generate lift through pressure differences.",
                "Aerodynamics is essential in aerospace engineering."
            ],

            # Chemistry
            "chemistry": [
                "Chemistry studies matter and its transformations.",
                "Atoms combine to form molecules.",
                "Chemical reactions involve bond changes.",
                "Chemistry connects physics and biology.",
                "Chemistry is central to material science."
            ],

            "atom": [
                "Atoms are the building blocks of matter.",
                "Atoms consist of protons, neutrons and electrons.",
                "The atomic number identifies an element.",
                "Electrons occupy energy levels.",
                "Atomic theory is fundamental to chemistry."
            ],

            # Motivation
            "motivation": [
                "Every expert was once a beginner.",
                "Small progress each day leads to big results.",
                "Consistency beats intensity.",
                "Learning never stops in technology.",
                "Keep building and keep improving."
            ],

            "study": [
                "Focus on understanding concepts, not memorization.",
                "Practice regularly for long-term retention.",
                "Break large goals into smaller tasks.",
                "Revision strengthens memory.",
                "Consistency creates success."
            ]
        }

         self.responses.update({

        "deep learning": [
        "Deep Learning uses neural networks with multiple layers.",
        "Deep Learning powers image recognition and modern AI systems.",
        "Convolutional Neural Networks are commonly used for images.",
        "Recurrent Neural Networks are useful for sequential data.",
        "Deep Learning requires large datasets and computing power."
        ],

    "data structure": [
        "Data structures organize and store data efficiently.",
        "Arrays, linked lists, stacks and queues are fundamental data structures.",
        "Choosing the right data structure improves performance.",
        "Trees and graphs are advanced data structures.",
        "Data structures are essential for software engineering."
    ],

    "algorithm": [
        "Algorithms are step-by-step procedures to solve problems.",
        "Efficient algorithms reduce execution time.",
        "Sorting and searching are common algorithm categories.",
        "Algorithms are the backbone of computer science.",
        "Optimization often focuses on algorithm efficiency."
    ],

    "operating system": [
        "An operating system manages hardware and software resources.",
        "Examples include Windows, Linux and Android.",
        "The OS handles memory, processes and file systems.",
        "Linux is widely used in servers and development.",
        "Operating systems provide an interface between users and hardware."
    ],

    "network": [
        "Computer networks allow devices to communicate.",
        "TCP/IP is the foundation of the internet.",
        "Routers direct data packets between networks.",
        "Networking is important for cybersecurity.",
        "Protocols define communication rules."
    ],

    "linux": [
        "Linux is a powerful open-source operating system.",
        "Linux is widely used in servers and cloud computing.",
        "Many cybersecurity tools run on Linux.",
        "Linux distributions include Ubuntu, Fedora and Debian.",
        "Learning Linux is valuable for developers and engineers."
    ],

    "database": [
        "Databases store and organize information efficiently.",
        "SQL is commonly used to manage databases.",
        "MySQL and PostgreSQL are popular database systems.",
        "Indexes improve database performance.",
        "Databases are essential for modern applications."
    ],

    "cloud": [
        "Cloud computing provides computing resources over the internet.",
        "Major cloud providers include AWS, Azure and Google Cloud.",
        "Cloud services improve scalability.",
        "Virtualization is important in cloud computing.",
        "Cloud skills are highly valuable."
    ],

    "aeronautics": [
        "Aeronautics focuses on aircraft design and flight.",
        "Aerodynamics plays a crucial role in aircraft performance.",
        "Lift, drag, thrust and weight are the four forces of flight.",
        "Aircraft stability is essential for safe operation.",
        "Aeronautical engineering combines physics and engineering."
    ],

    "airfoil": [
        "An airfoil is designed to generate lift.",
        "Airfoil shape affects aerodynamic performance.",
        "Camber influences lift characteristics.",
        "Airfoils are used in wings and propellers.",
        "NACA airfoils are commonly studied."
    ],

    "lift": [
        "Lift is the force that opposes weight.",
        "Lift is generated due to pressure differences around an airfoil.",
        "Aircraft require sufficient lift for flight.",
        "Angle of attack affects lift generation.",
        "Lift depends on air density, velocity and wing area."
    ],

    "drag": [
        "Drag opposes the motion of an aircraft.",
        "Parasitic drag and induced drag are major categories.",
        "Reducing drag improves efficiency.",
        "Aerodynamic design aims to minimize drag.",
        "Drag increases with speed."
    ],

    "bernoulli": [
        "Bernoulli's principle relates pressure and velocity in fluid flow.",
        "Higher fluid velocity corresponds to lower pressure.",
        "Bernoulli's principle helps explain lift generation.",
        "Fluid dynamics relies heavily on Bernoulli's equation.",
        "Aircraft wings utilize pressure differences."
    ],

    "newton law": [
        "Newton's First Law is the law of inertia.",
        "Newton's Second Law states F = ma.",
        "Newton's Third Law states every action has an equal and opposite reaction.",
        "Rocket propulsion demonstrates Newton's Third Law.",
        "Newtonian mechanics is fundamental in engineering."
    ],

    "thermodynamics": [
        "Thermodynamics studies heat and energy transfer.",
        "The First Law relates to energy conservation.",
        "The Second Law introduces entropy.",
        "Thermodynamics is important in engines and aerospace.",
        "Heat engines operate using thermodynamic cycles."
    ],

    "chemistry": [
        "Chemistry studies matter and chemical transformations.",
        "Atoms combine to form molecules.",
        "Chemical reactions involve bond changes.",
        "Chemistry is central to material science.",
        "Understanding chemistry helps in engineering applications."
    ],

    "periodic table": [
        "The periodic table organizes elements by atomic number.",
        "Elements in the same group have similar properties.",
        "The periodic table is fundamental in chemistry.",
        "Metals, non-metals and metalloids are major categories.",
        "Chemical behavior depends on electron configuration."
    ],

    "trigonometry": [
        "Trigonometry studies relationships between angles and sides.",
        "Sine, cosine and tangent are fundamental functions.",
        "Trigonometry is widely used in engineering.",
        "Aircraft navigation uses trigonometric calculations.",
        "Practice improves trigonometry skills."
    ],

    "calculus": [
        "Calculus studies rates of change and accumulation.",
        "Differentiation measures change.",
        "Integration measures accumulation.",
        "Calculus is essential for engineering analysis.",
        "Many physical laws are expressed using calculus."
    ],

    "motivation": [
        "Consistency beats intensity.",
        "Small progress each day leads to great results.",
        "Every expert was once a beginner.",
        "Build projects to improve your skills.",
        "Learning compounds over time."
    ],

    "study": [
        "Study with focus and consistency.",
        "Practice active recall and revision.",
        "Break complex topics into smaller parts.",
        "Use projects to reinforce learning.",
        "Understanding is better than memorization."
    ]
})
    
   
         self.fallback_responses = [

    "I can help with AI, Programming, Cybersecurity, Mathematics, Physics, Chemistry and Aeronautical Engineering.",

    "Try asking about Python, Java, Android, Robotics or Aerodynamics.",

    "Interesting question. Could you provide more details?",

    "I am an offline study assistant focused on technology and science.",

    "Let's explore that topic together.",

    "Could you rephrase your question?",

    "I specialize in engineering, technology and future innovation.",

    "Ask me about aircraft, programming, AI or mathematics.",

    "Learning starts with curiosity.",

    "I am always ready to discuss science and technology."
]

    def get_response(self, user_message):

        user_message = user_message.lower().strip()

        # Greetings
        if user_message in [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening"
        ]:
            return random.choice(self.greetings)

        # Quiz Mode
        if "quiz" in user_message:

            if "python" in user_message:
                return random.choice(self.quizzes["python"])

            if "ai" in user_message:
                return random.choice(self.quizzes["ai"])

            if "physics" in user_message:
                return random.choice(self.quizzes["physics"])

            return "Available quizzes: AI, Python, Physics"

        # Formula Mode
        for key, value in self.formulas.items():

            if key in user_message:
                return value

        # Study Topics
        for topic, explanation in self.study_topics.items():

            if topic in user_message:
                return explanation

        # Keyword Matching
        matched_responses = []

        for keyword, responses in self.responses.items():

            if keyword in user_message:
                matched_responses.extend(responses)

        if matched_responses:
            return random.choice(matched_responses)

        # Calculator
        try:

            if any(op in user_message for op in ["+", "-", "*", "/", "%"]):

                expression = user_message.replace("what is", "").strip()

                result = eval(expression)

                return f"The answer is {result}"

        except:
            pass

        # Fallback
        return random.choice(self.fallback_responses)

