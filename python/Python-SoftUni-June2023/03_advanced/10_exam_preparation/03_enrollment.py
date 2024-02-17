def gather_credits(credits_number, *args):
    curr_credits = 0
    courses_enrolled = {}

    for course_name, course_credits in args:

        if curr_credits >= credits_number:
            break

        if course_name not in courses_enrolled:
            courses_enrolled[course_name] = course_credits
            curr_credits += course_credits

    if curr_credits >= credits_number:
        return (f'Enrollment finished! Maximum credits: {curr_credits}.\n'
                f'Courses: {", ".join(sorted(courses_enrolled))}')

    return f'You need to enroll in more courses! You have to gather {credits_number - curr_credits} credits more.'

print(gather_credits(
 60,
 ("Basics", 27),
 ("Fundamentals", 27),
 ("Advanced", 30),
 ("Web", 30)
))

{:  for  in }
