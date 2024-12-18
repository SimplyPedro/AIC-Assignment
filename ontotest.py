import tkinter as tk
from tkinter import messagebox
from owlready2 import *


from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    response = {
        "Answer": [],
        "Media": [],
        "Pedagigical_Support": [],
        "Question": [],
        "Summary": [],
        "User": []
    }
    
    # Load the ontology
    ontology_path = "OntoIts1.ttl"
    onto = get_ontology(ontology_path).load()
    print("Ontology loaded successfully!")

    # Display ontology structure
    print("\nClasses in the Ontology:")
    for cls in onto.classes():
        print(cls)

    print("\nObject Properties:")
    for prop in onto.object_properties():
        print(prop)

    print("\nData Properties:")
    for dprop in onto.data_properties():
        print(dprop)

    print("\nIndividuals in the Ontology:")
    for individual in onto.individuals():
        print(individual)

# Access specific individual and their properties
    if hasattr(onto, 'Peter'):
        peter = onto.Peter
        print("\nDetails for Individual 'Peter':")
        print(f"Name: {getattr(peter, 'name', ['Unknown'])[0]}")
        print(f"Score: {getattr(peter, 'score', ['Unknown'])[0]}")
    if hasattr(peter, 'attempts'):
        print(f"Attempts: {[quiz.name[0] for quiz in peter.attempts]}")
    else:
        print("\nIndividual 'Peter' does not exist in the ontology.")

    # Access specific quiz
    if hasattr(onto, 'Chemistry'):
        chemistry_quiz = onto.Chemistry
        print("\nQuiz Information:")
        print(f"Title: {getattr(chemistry_quiz, 'title', ['Unknown'])[0]}")
        print(f"Passing Score: {getattr(chemistry_quiz, 'passingScore', ['Unknown'])[0]}")

    # Access questions and answers
    if hasattr(onto, 'Question1') and hasattr(onto, 'Answer1'):
        question1 = onto.Question1
        print("\nQuestion and Answer Relationships:")
        print(f"Question Text: {getattr(question1, 'text', ['Unknown'])[0]}")
        print(f"Hint: {getattr(question1, 'hint', ['Unknown'])[0]}")

    correct_answer = onto.Answer1
    print(f"Correct Answer: {getattr(correct_answer, 'text', ['Unknown'])[0]} (isCorrect: {getattr(correct_answer, 'isCorrect', ['Unknown'])[0]})")
    else:
        print("\nQuestions or answers not found in the ontology.")


    # Perform reasoning
    print("\nReasoning with HermiT:")
    try:
        with onto:
        sync_reasoner()
    print("Reasoning completed successfully. Ontology is consistent.")
        except Exception as e:
           print(f"Reasoning failed: {e}")
