# Home Access Center Grade Checker
Easily get json object of your grades if your school uses home access center.

<h3>How to use</h3>
<p>Drag <code>gradecheck.py</code> into the root of your program directory, then use <code>from gradecheck import grades</code>. Create a <code>grade</code> object like so:</p>

```
from gradecheck import grades

# create the object like this (without the brackets):
grades = grades('[your_username]', '[your_password]', '[home access center base url]')

# fetch your grades. returns a dictionary with class names, your grade, your teacher, and their email.
my_grades = grades.fetch()


```
