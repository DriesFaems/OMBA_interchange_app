import pandas as pd
import streamlit as st

st.title('OMBA Course Interchange Overview')

# Load data

synch = pd.read_excel('Synch courses.xlsx')
asynch = pd.read_excel('Asynch courses.xlsx')
start_data = pd.read_excel('Example database.xlsx')

# create subtitle

st.subheader('This application provides an overview of which courses you have completed and skipped, and which courses you can still interchange')

# ask user to provide their name

# create a list of names

names = start_data['Name'].unique()

# create a dropdown menu for the names

name_input = st.selectbox('Please select your name', names)

# filter data based on user input

data = start_data[start_data['Name'] == name_input]

# count the number of values for each module in the synch courses

synch_count = synch['Module'].value_counts()

# turn the series into a dataframe

synch_count = synch_count.reset_index()

# create list of finished courses

finished_courses_meta_list = []

# iterate over the rows of the dataframe

for i in range(data.shape[0]):
    if data['Courses Finished'].iloc[i] != data['Courses Finished'].iloc[i]:
        finished_courses = []
    else:
        finished_courses = data['Courses Finished'].iloc[i].split('; ')
        finished_courses_meta_list.append(finished_courses)

# create a list of Module Courses Finished

finished_modules_meta_list = []

# iterate over the rows of the dataframe

for i in range(data.shape[0]):
    if data['Module Courses Finished'].iloc[i] != data['Module Courses Finished'].iloc[i]:
        finished_modules = []
    else:
        finished_modules = data['Module Courses Finished'].iloc[i].split('; ')
        finished_modules_meta_list.append(finished_modules)

# create a list of skipped courses

skipped_courses_meta_list = []

# iterate over the rows of the dataframe

for i in range(data.shape[0]):
    if data['Courses Skipped'].iloc[i] != data['Courses Skipped'].iloc[i]:
        skipped_courses = []
    else:
        skipped_courses = data['Courses Skipped'].iloc[i].split('; ')
        skipped_courses_meta_list.append(skipped_courses)

#create a list of Module Courses Skipped

skipped_modules_meta_list = []

# iterate over the rows of the dataframe

for i in range(data.shape[0]):
    if data['Module Courses Skipped'].iloc[i] != data['Module Courses Skipped'].iloc[i]:
        skipped_modules = []
    else:
        skipped_modules = data['Module Courses Skipped'].iloc[i].split('; ')
        skipped_modules_meta_list.append(skipped_modules)

# create a list of asynchronou courses

asynch_courses_meta_list = []

# iterate over the rows of the dataframe

for i in range(data.shape[0]):
    if data['Asynchronous Courses Finished'].iloc[i] != data['Asynchronous Courses Finished'].iloc[i]:
        asynch_courses = []
    else:
        asynch_courses = data['Asynchronous Courses Finished'].iloc[i].split('; ')
        asynch_courses_meta_list.append(asynch_courses)



# create click button to show user data

if st.button('Show my data'):
    # print out for first observation for each module which courses have been finished
    st.markdown('**Overvew of finished courses for each module**')
    number_of_finished_courses = len(finished_courses_meta_list[0])
    st.write(f'{name_input} has finished {number_of_finished_courses} courses')
    all_modules = synch['Module'].unique()
    for i in range(len(all_modules)):
        module = all_modules[i]
        if module not in finished_modules_meta_list[0]:
            st.write(f'{i+1}: {module}: No courses have been finished')
        else:
            courses = ''
            for j in range(len(finished_modules_meta_list[0])):
                if module in finished_modules_meta_list[0][j]:
                    if courses == '':
                        courses = (finished_courses_meta_list[0][j])
                    else:
                        courses = courses + '; ' + (finished_courses_meta_list[0][j])
            st.write(f'{i+1}: {module}: {courses}')
    st.markdown('**Overview of skipped courses for each module**')
    # count the number of skipped courses
    number_of_skipped_courses = len(skipped_courses_meta_list[0])
    # for first observation print the skipped courses
    st.write(f'{name_input} has skipped {number_of_skipped_courses} courses')
    for i in range(len(all_modules)):
        module = all_modules[i]
        if module not in skipped_modules_meta_list[0]:
            st.write(f'{i+1}: {module}: No courses have been skipped')
        else:
            courses = ''
            for j in range(len(skipped_modules_meta_list[0])):
                if module in skipped_modules_meta_list[0][j]:
                    if courses == '':
                        courses = (skipped_courses_meta_list[0][j])
                    else:
                        courses = courses + '; ' + (skipped_courses_meta_list[0][j])
            st.write(f'{i+1}: {module}: {courses}')

    st.markdown('**Overview of Asynchronous courses**')
    # count the number of asynchronous courses have geen followed
    number_of_asynch_courses = len(asynch_courses_meta_list[0])
    # for first observation print the asynchronous courses that have been followed
    if number_of_asynch_courses == 0:
        st.write(f'{name_input} has not followed any asynchronous courses')
    else:
        courses = ''
        for i in range(len(asynch_courses_meta_list[0])):
            if courses == '':
                courses = (asynch_courses_meta_list[0][i])
            else:
                courses = courses + '; ' + (asynch_courses_meta_list[0][i])
    st.write(f'{name_input} has followed {number_of_asynch_courses} asynchronous course(s): {courses}')
    st.markdown('**Status international module**')
    if data['International Module'].iloc[0] == 'Yes':
        International = 1
        st.write(f'{name_input} has followed the international module')
    else:
        International = 0
        st.write(f'{name_input} has not followed the international module')
    # calculate and report the number of interchanges
    st.markdown('**Number of interchanges that are still available**')
    asynch_interchanges = 3 - number_of_asynch_courses
    if data['International Module'].iloc[0] == 'Yes':
        st.write(f'{name_input} can still interchange {asynch_interchanges} courses')
    else:
        st.write(f'{name_input} can still interchange {asynch_interchanges} courses and follow 1 international module')
    # for each module, provide an overview of which courses can still be interchanged
    st.markdown('**Overview of courses that can still be interchanged per module**')
    for i in range(len(all_modules)):
        module = all_modules[i]
        #count the number of finished courses for the module
        number_of_finished_courses_module = 0
        for j in range(len(finished_modules_meta_list[0])):
            if module in finished_modules_meta_list[0][j]:
                number_of_finished_courses_module += 1
        #count the number of skipped courses for the module
        number_of_skipped_courses_module = 0
        for j in range(len(skipped_modules_meta_list[0])):
            if module in skipped_modules_meta_list[0][j]:
                number_of_skipped_courses_module += 1
        if number_of_skipped_courses_module > 0 or number_of_finished_courses_module == synch_count['Module'].loc[i]:
            st.write(f'{i+1}: {module}: You can no longer interchange courses for this module')
        else: 
            # select from synch the courses that belong to the module 
            module_courses = synch[synch['Module'] == module]
            # iterate over the courses in the module
            courses = ''
            for j in range(module_courses.shape[0]):
                course = module_courses['Course Titles'].iloc[j]
                if course not in finished_courses_meta_list[0] and course not in skipped_courses_meta_list[0]:
                    if courses == '':
                        courses = course
                    else:
                        courses = courses + '; ' + course
            st.write(f'{i+1}: {module}: Courses that can still be interchanged: {courses}')
else:
    st.write('Please click the button to show your data')