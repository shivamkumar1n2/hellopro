import google.generativeai as genai

genai.configure(api_key="AIzaSyATFOnWJVjmCierSGOsacFs8ilcTrI9B5g")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("write code for kmeans")
print(response.text)
