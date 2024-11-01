from flask import Flask, render_template, request

app = Flask(__name__)

class SkillDevelopmentPlatform:
    def __init__(self):
        # Expanded list of skills
        self.questions = {
            "Python": 0,
            "Java": 0,
            "C++": 0,
            "JavaScript": 0,
            "SQL": 0,
            "HTML/CSS": 0,
            "Data Analysis": 0,
            "Machine Learning": 0,
            "Communication Skills": 0,
            "Team Collaboration": 0,
            "Problem Solving": 0,
            "Time Management": 0,
            "Critical Thinking": 0,
            "Adaptability": 0,
            "Project Management": 0,
            "Negotiation": 0,
            "Leadership": 0,
            "Creativity": 0,
            "Networking": 0,
            "Customer Service": 0,
            "Public Speaking": 0,
            "Digital Marketing": 0,
            "Cloud Computing": 0,
            "Cybersecurity": 0,
            "UX/UI Design": 0,
            "Data Visualization": 0,
            "Business Analytics": 0,
            "Artificial Intelligence": 0,
            "DevOps": 0,
        }

        self.industry_standards = {
            "Python": 8,
            "Java": 7,
            "C++": 7,
            "JavaScript": 8,
            "SQL": 7,
            "HTML/CSS": 6,
            "Data Analysis": 7,
            "Machine Learning": 8,
            "Communication Skills": 9,
            "Team Collaboration": 8,
            "Problem Solving": 8,
            "Time Management": 8,
            "Critical Thinking": 8,
            "Adaptability": 9,
            "Project Management": 8,
            "Negotiation": 7,
            "Leadership": 8,
            "Creativity": 7,
            "Networking": 7,
            "Customer Service": 8,
            "Public Speaking": 8,
            "Digital Marketing": 7,
            "Cloud Computing": 7,
            "Cybersecurity": 8,
            "UX/UI Design": 7,
            "Data Visualization": 7,
            "Business Analytics": 7,
            "Artificial Intelligence": 8,
            "DevOps": 7,
        }

        self.course_database = {
            "Python": ["Python for Beginners", "Advanced Python Programming"],
            "Java": ["Java Fundamentals", "Java for Android Development"],
            "C++": ["Introduction to C++", "C++ Advanced Techniques"],
            "JavaScript": ["JavaScript Basics", "Front-end Development with JavaScript"],
            "SQL": ["SQL for Data Science", "Advanced SQL Queries"],
            "HTML/CSS": ["HTML5 and CSS3", "Responsive Web Design"],
            "Data Analysis": ["Data Analysis with Python", "Data Visualization Techniques"],
            "Machine Learning": ["Machine Learning Basics", "Deep Learning Specialization"],
            "Communication Skills": ["Effective Communication Skills", "Business Communication"],
            "Team Collaboration": ["Team Collaboration Strategies", "Building Effective Teams"],
            "Problem Solving": ["Problem Solving Techniques", "Logical Reasoning Skills"],
            "Time Management": ["Time Management Essentials", "Productivity Hacks"],
            "Critical Thinking": ["Critical Thinking Skills", "Analytical Thinking"],
            "Adaptability": ["Adapting to Change", "Learning Agility in the Workplace"],
            "Project Management": ["Project Management Fundamentals", "Agile Project Management"],
            "Negotiation": ["Negotiation Skills Workshop", "Advanced Negotiation Techniques"],
            "Leadership": ["Leadership Skills Development", "Transformational Leadership"],
            "Creativity": ["Creative Thinking Techniques", "Innovation in the Workplace"],
            "Networking": ["Networking Skills for Professionals", "Building Professional Relationships"],
            "Customer Service": ["Customer Service Excellence", "Handling Difficult Customers"],
            "Public Speaking": ["Public Speaking for Beginners", "Mastering the Art of Public Speaking"],
            "Digital Marketing": ["Digital Marketing Basics", "Advanced Digital Marketing Strategies"],
            "Cloud Computing": ["Introduction to Cloud Computing", "Cloud Architecture Fundamentals"],
            "Cybersecurity": ["Cybersecurity Basics", "Advanced Cybersecurity Strategies"],
            "UX/UI Design": ["Introduction to UX/UI Design", "Design Thinking for UX"],
            "Data Visualization": ["Data Visualization with Python", "Tableau for Data Visualization"],
            "Business Analytics": ["Business Analytics Fundamentals", "Advanced Business Analytics"],
            "Artificial Intelligence": ["AI Fundamentals", "Machine Learning and AI Applications"],
            "DevOps": ["DevOps Basics", "Implementing DevOps in Organizations"],
        }

    def assess_skills(self, ratings):
        for skill, rating in ratings.items():
            self.questions[skill] = int(rating)

    def identify_skill_gaps(self):
        gaps = {}
        for skill, proficiency in self.questions.items():
            if proficiency < self.industry_standards[skill]:
                gaps[skill] = self.industry_standards[skill] - proficiency
        return gaps

    def recommend_courses(self, skill_gaps):
        recommendations = {}
        for skill in skill_gaps.keys():
            recommendations[skill] = self.course_database.get(skill, [])
        return recommendations

@app.route("/", methods=["GET", "POST"])
def index():
    platform = SkillDevelopmentPlatform()

    if request.method == "POST":
        # Step 1: Assess Skills
        ratings = request.form.to_dict()
        platform.assess_skills(ratings)

        # Step 2: Identify Skill Gaps
        skill_gaps = platform.identify_skill_gaps()
        recommendations = platform.recommend_courses(skill_gaps)

        return render_template("index.html", gaps=skill_gaps, recommendations=recommendations)

    return render_template("index.html", gaps=None, recommendations=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
