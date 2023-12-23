# Optical Mark Recognition - OMR sheet Scanner (Scantron tests)

- Optical Mark Recognition, or OMR, is the process of automatically analyzong human-marked documents and interpreting their results.
- The most easily recognizable form of OMR are the bubble sheet multiple choice tests.

## Steps to build a bubble sheet Scanner and Grader

1. Detect the exam in an image
2. Apply perspective transform to extract the top-down, birds-eye-view of the exam
3. Extract the set of bubbles (possible answer choices) from the perspective transformed exam
4. Sort the questions/bubbles into rows
5. Determine the marked (bubbled in) answer for each row.
6. Lookup the correct answer in our answer key to determine if the user was correct in their choice.
7. Repeat for all questions in the exam.

