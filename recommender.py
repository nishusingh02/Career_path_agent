from genai import interpret_career_goal

def get_recommendations(employee_data):
    goal = employee_data.get("career_goal", "")
    if goal:
        # Use GenAI to interpret the career goal and generate recommendations
        genai_result = interpret_career_goal(goal)
        # If GenAI returns valid recommendations, use them
        if (
            isinstance(genai_result, dict)
            and "learning_paths" in genai_result
            and "job_rotations" in genai_result
        ):
            return genai_result
    # Fallback: simple rule-based logic
    experience = employee_data.get("experience", 0)
    rating = employee_data.get("performance_rating", 0)
    recommendations = {
        "learning_paths": [],
        "job_rotations": []
    }
    if "leadership" in goal.lower():
        recommendations["learning_paths"].append("Leadership Essentials (Coursera)")
        if experience > 3 and rating > 4:
            recommendations["job_rotations"].append("Team Lead (Any Department)")
    if "technical" in goal.lower():
        recommendations["learning_paths"].append("Advanced Python (Udemy)")
        if experience > 2:
            recommendations["job_rotations"].append("Senior Developer (Engineering)")
    if not recommendations["learning_paths"]:
        recommendations["learning_paths"].append("General Professional Development")
    if not recommendations["job_rotations"]:
        recommendations["job_rotations"].append("Explore cross-functional teams")
    return recommendations