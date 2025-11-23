from django.shortcuts import render

TEAM = [
  { 'id':'arlington', 'name':'Arlington (Link) Kell', 'role':'Fullstack / Maps', 'avatar':'/static/LinkArlington.jpg',
    'contrib':'Link is a third-year computer science student at Georgia Tech with a focus on frontend development and user interface design. Link enjoys experimenting with motion design, working on personal web projects, and contributing to open-source design systems.',
    'skills':['Django', 'Python', 'Git', 'GitHub'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/arlingtonmkell'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/arlington-kell/'}
    ],
    'work':[
      {
        'title': 'Application Pipeline API',
        'desc': 'Developed the back-end API for the application tracking pipeline, enabling both recruiters and job seekers to manage and update application states (e.g., Applied, Review, Interview) on their respective Kanban boards.'
      }
    ]
  },
  { 'id':'focus', 'name':'Chayanat (Focus) Tanjariyaporn', 'role':'Fullstack', 'avatar':'https://static.wixstatic.com/media/e3397d_862ca9a1ea3640f1933d8b824a43aa11~mv2.png',
    'contrib':'Chayanat is a second-year computer science student at Georgia Tech. Being from Thailand, he also goes by his nickname, "Focus". His interests generally lies in human-computer interactions, non-traditional computer interfaces, and extended reality technologies. He is a member of GTXR (Georgia Tech Extended Reality, not Georgia Tech Experimental Rocketry!), as well as a student advisor for First-Year Texperience, a First-Year Leadership Organization on campus.',
    'skills':['Django', 'Python', 'Git', 'GitHub'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/TChayanat'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/tchayanat/'}
    ],
    'work':[
      {
        'title': 'Administrator Functionality',
        'desc': 'Developed core administrator functionalities, including user role management and content moderation tools to ensure platform safety and fairness.'
      },
      {
        'title': 'Geospatial Features',
        'desc': 'Engineered the back-end logic for the map-based search feature, enabling efficient geospatial querying of job postings and candidate locations.'
      },
      {
        'title': 'Communication Systems',
        'desc': 'Built the back-end for the real-time, in-platform messaging system, allowing direct communication between recruiters and job seekers.'
      },
      {
        'title': 'Notification Services',
        'desc': 'Integrated an email service to handle automated platform notifications and enable recruiter outreach to candidates via their personal email.'
      }
    ]
  },
  { 'id':'david', 'name':'David Elman', 'role':'Backend / Product Manager', 'avatar':'https://static.wixstatic.com/media/e3397d_ca797d21eea0435abf3ae5d94cef5dfe~mv2.jpg',
    'contrib':'David is a third year computer science student at Georgia Tech, with threads in Infonetworks and Cybersecurity. He is local to the area, growing up in Marietta, Georgia. Though he is currently studying internet and cybersecurity, he also has an interest in computer hardware and hopes to get a Master\'s degree in Computer Engineering. Currently he participates in the Embedded Systems Cybersecurity VIP through GTRI and has also participated in Residence Hall Association and VGDev.',
    'skills':['Django', 'Python', 'Git', 'GitHub'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/DavidElman23'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/david-elman-43598426a/'}
    ],
    'work':[
      {
        'title': 'Quality Assurance & Debugging',
        'desc': 'Managed back-end quality assurance, proactively identifying and resolving critical bugs across the application to ensure stability and performance.'
      },
      {
        'title': 'Recommendation Engine (Jobs)',
        'desc': 'Designed and implemented the recommendation algorithm for job seekers, intelligently matching user profiles and skills to relevant job opportunities.'
      },
      {
        'title': 'Recommendation Engine (Candidates)',
        'desc': 'Developed the candidate recommendation algorithm for recruiters, surfacing qualified talent by analyzing job posting requirements against the user database.'
      }
    ]
  },
  { 'id':'James', 'name':'James Armendariz', 'role':'Backend', 'avatar':'https://static.wixstatic.com/media/e3397d_0b4fd40ae0604b07a5e39c3411175ef2~mv2.jpg',
    'contrib':'James is a second year computer science student at Georgia Tech, concentrating in Information Internetworks and Cybersecurity. He\'s from in-state, Buford, Georgia. Aside from his engagement in cybersecurity related threads, he has a strong interest in artificial intelligence and it\'s applications among various fields; he hopes to pursue a field in either cybersecurity or AI. He\'s looking to engage in various internship opportunities to gain any relevant workplace experience in CS.',
    'skills':['Django', 'Python', 'Git', 'GitHub'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/james-armendariz'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/james-armendariz-b04a92220/'}
    ],
    'work':[
      {
        'title': 'User Profile & Application API',
        'desc': 'Developed the back-end services for creating, updating, and securing user profiles, including the core \'one-click apply\' functionality for job applications.'
      },
      {
        'title': 'Recruiter Tools API',
        'desc': 'Built the back-end API endpoints for the recruiter dashboard, enabling recruiters to post, edit, and manage their job listings.'
      },
      {
        'title': 'Core Platform Integration',
        'desc': 'Led the integration of all user-specific modules (Profile, Jobs, Applications) into a single, centralized dashboard to create a cohesive and seamless user experience.'
      }
    ]
  },
  { 'id':'Sandro', 'name':'Sandro Karkusashvili', 'role':'Frontend', 'avatar':'https://static.wixstatic.com/media/e3397d_c1c86c2d36cb46a2b39cfc9c3d1cd503~mv2.png',
    'contrib':'Sandro is a third-year computer science student at Georgia Tech, with threads in People and Infonetworks. He was born in Tbilisi, Georgia and lived in New York City for 7 years before coming to Atlanta. His interest lies in UI/UX design and frontend implementation, and connecting programs to people. In free time, he likes to make coding projects, play soccer, and workout.',
    'skills':['Django', 'Python', 'Git', 'GitHub', 'Figma'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/sandro21'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/sandroka/'}
    ],
    'work':[
      {
        'title': 'Front-End Lead',
        'desc': 'Spearheaded all front-end development, translating design mockups into responsive, high-fidelity UI components and guiding the team on UI/UX best practices.'
      },
      {
        'title': 'UI/UX Implementation',
        'desc': 'Designed and implemented the application\'s main landing page and established the comprehensive visual theme, color palette, and style guide used across all pages.'
      }
    ]
  },
  { 'id':'ali', 'name':'Ali Vafaeian', 'role':'Fullstack / Scrum Master', 'avatar':'https://static.wixstatic.com/media/e3397d_df1ad885153246048164f4d0ec283889~mv2.jpg',
    'contrib':'Ali Vafaeian is a fourth-year Computer Science student at Georgia Tech with a focus on AI and interactive media. He\'s a front-end-leaning builder who likes turning complex systems into clean, intuitive interfaces often at the intersection of graphics, game engines, and machine learning. Recent work includes training reinforcement-learning agents in Unity ML-Agents (PPO/SAC) to navigate dynamic environments, engineering a seed-based gameplay randomizer across UE4/C++/Lua, and shipping a fullstack Django storefront.',
    'skills':['Django', 'Python', 'Git', 'GitHub'],
    'links':[
      {'label':'GitHub', 'href':'https://github.com/Criticp'},
      {'label':'LinkedIn', 'href':'https://www.linkedin.com/in/vafaeianali/'}
    ],
    'work': [
      {
        'title': 'Administrator Features & Data',
        'desc': 'Developed the administrator-facing data export feature, allowing for CSV downloads of user and job data for reporting and analysis.'
      },
      {
        'title': 'Project & Workflow Management',
        'desc': 'Managed the team\'s version control by organizing the GitHub repository and standardizing development workflows and communication channels.'
      },
      {
        'title': 'System Design',
        'desc': 'Authored key system design diagrams (e.g., UML, data flow) to guide development, document architecture, and ensure a shared technical vision.'
      },
      {
        'title': 'UI/UX & Feature Implementation',
        'desc': 'Implemented the front-end for the job seeker\'s \'Application Tracker,\' visualizing application statuses in a dynamic, drag-and-drop Kanban board.'
      },
      {
        'title': 'Core UI & Authentication',
        'desc': 'Led the UI/UX design for the main user dashboard and profile pages and engineered the secure user authentication and session management flow.'
      }
    ]
  }
]

def home(request):
    return render(request, 'home.html')

def team(request):
    return render(request, 'team.html', {'team': TEAM})

def member(request, member_id):
    member_data = next((m for m in TEAM if m['id'] == member_id), None)
    return render(request, 'member.html', {'member': member_data})

def system(request):
    return render(request, 'system.html')

def process(request):
    return render(request, 'process.html')

def video(request):
    return render(request, 'video.html')

def contact(request):
    return render(request, 'contact.html')

