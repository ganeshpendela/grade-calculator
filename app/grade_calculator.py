
# Python module for copying objects
import copy

# Importing application internal classes
from grades import Grades
from grade_weights import GradeWeights

class GradeCalculator:
    """
    Calculates the overall course grade for ENPM611.
    """
    
    @staticmethod
    def calculate_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """"
        Calculates the percentace of the overall course
        grade. If not all grades have been set yet, this
        function returns None.
        """
        if grades.quiz_1 is None or grades.quiz_2 is None or grades.midterm is None or grades.project is None or grades.final is None:
            print("Can't calculate final grade without all assignments graded")
            return None
        else:
            quizzes_part = ((grades.quiz_1 + grades.quiz_2) / 2) * weights.quizzes
            midterm_part = grades.midterm * weights.midterm
            project_part = grades.project * weights.project
            final_part = grades.final * weights.final
            course_grade = quizzes_part + midterm_part + project_part + final_part
            return course_grade
        
        
        
    @staticmethod
    def calculate_optimistic_course_percentage(grades:Grades, weights:GradeWeights) -> float:
        """
        Calculates the course percentage grade assuming that
        all assignments that have not been completed receive 100%. 
        """
        
        # Need to create a copy so that we don't overwrite
        # the values of the Grades object that was passed in
        optimistic_grades:Grades = copy.copy(grades)
        
        # Now we are setting all grades that have not been set
        # to the maximum percentage of 100%
        if optimistic_grades.quiz_1 is None:
            optimistic_grades.quiz_1 = 1
        if optimistic_grades.quiz_2 is None:
            optimistic_grades.quiz_2 = 1
        if optimistic_grades.midterm is None:
            optimistic_grades.midterm = 1
        if optimistic_grades.project is None:
            optimistic_grades.project = 1
        if optimistic_grades.final is None:
            optimistic_grades.final = 1
        
        # Let the basic calculation function take care of actually
        # calculating the percentage grade
        return GradeCalculator.calculate_course_percentage(optimistic_grades, weights)
        
    @staticmethod
    def calculate_letter_grade(percentage_grade:float) -> str:
        """
        Calculate the letter grade giving a percentage grade.
        The cutoffs for letter grades can be found in the introductory slides
        and in the syllabus.
        """
        
        # Avoid exception due to missing value
        if percentage_grade is None:
            return None
        
        # Return the letter that corresponds to
        # the percentage cutoff
        if percentage_grade >= 0.91:
            return 'A'
        elif percentage_grade >= 0.8:
            return 'B'
        elif percentage_grade >= 0.74:
            return 'C'
        elif percentage_grade >= 0.6:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def minimum_average_points(grades:Grades, weights:GradeWeights):
        """"
        calculates the minimum average points for all yet ungraded
        assignments to still get an A in class
        """
        present_coursegrade=0
        total_nongradedmarks=0
        graded_assignments=[]
        non_grades_assignments=[]
        if grades.quiz_1 is None:
            non_grades_assignments.append("quiz_1")
            total_nongradedmarks+=(weights.quizzes)/2
        elif grades.quiz_1!=None:
            graded_assignments.append("quiz_1")
            present_coursegrade+=((grades.quiz_1)/2) * weights.quizzes
        if grades.quiz_2 is None:
            non_grades_assignments.append("quiz_2")
            total_nongradedmarks+=(weights.quizzes)/2
        elif grades.quiz_2!=None:
            graded_assignments.append("quiz_2")
            present_coursegrade+=((grades.quiz_2)/2) * weights.quizzes
        if grades.midterm is None:
            non_grades_assignments.append("midterm")
            total_nongradedmarks+=weights.midterm
        elif grades.midterm!=None:
            graded_assignments.append("midterm")
            present_coursegrade+=grades.midterm * weights.midterm
        if grades.project is None:
            non_grades_assignments.append("project")
            total_nongradedmarks+=weights.project
        elif grades.project!=None:
            graded_assignments.append("project")
            present_coursegrade+=grades.project * weights.project
        if grades.final is None:
            non_grades_assignments.append("final")
            total_nongradedmarks+=weights.project
        elif grades.final!=None:
            graded_assignments.append("final")
            present_coursegrade+=grades.final*weights.final
        print("Graded Assignments are : ", graded_assignments)
        print("Non Graded Assignments are : ", non_grades_assignments)
        print("Your Present Course Grade : ", present_coursegrade)
        needed_percentage=0.91-present_coursegrade
        if(total_nongradedmarks<needed_percentage):
            print("You cannot get a A grade even you score full marks in next assignments")
        else:   
            print("needed total points you get in all the remaining assignment is : ",needed_percentage)

        
        

        