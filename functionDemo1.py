def student_info(**details):
  for key,value in details.items():
    print(f'{key}:{value}')

student_info(name="dammar",age=23,section="A",city="mahendranagar")