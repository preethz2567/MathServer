# Ex.05 Design a Website for Server Side Processing
## Date:23-11-2024

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
``` 
<html>
    <head>
        <title>FindPower</title>
    </head>
    <body>
        <table align="center" width="100%" bgcolor="#4682b4">
            <tr>
                <td align="center">
                    <h1>Power Calculator</h1>
                    <h2> - Preethi D (24007817)</h2>
                </td>
            </tr>
        </table>

     
        <hr>

        <p align="justify">
      
Power is a fundamental physical quantity that represents the rate at which work is done or energy is transferred over time. In the context of electrical circuits, power is calculated using the formula: P = I<sup>2</sup>R Where P is the power in watts, I is the intensity (current) in amperes, and R is the resistance in ohms. Intensity (I) refers to the flow of electric charge through a conductor, measured in amperes. It represents how much charge is flowing through the circuit per unit of time. Resistance (R), on the other hand, measures the opposition to the flow of electric current within the circuit, and it depends on the material, temperature, and dimensions of the conductor. The power dissipated in a circuit increases with higher current or resistance. By knowing both intensity and resistance, we can determine the power consumed by electrical devices, which is crucial for designing efficient electrical systems and understanding energy consumption.
        </p>

       
        <div class="form-container">
            <h2>Try it yourself 🚀</h2>

            <form method="POST">
                {% csrf_token %}
                <div class="form-group">
                    <label for="intensity">Intensity (I): (in Amperes)</label>
                    <input type="number" id="intensity" name="Intensity" placeholder="Enter Intensity (I)" value="{{I }}">
                  
                </div>
                <div class="form-group">
                    <label for="resistance">Resistance (R):(In ohms)</label>
                    <input type="number" id="resistance" name="Resistance" placeholder="Enter Resistance (R)" value="{{R}}">
                  
                </div>
                <div class="form-group">
                    <label for="power">Power (P): (In watts)</label>
                    <input type="text" id="power" name="Power" placeholder="Power (P)" value="{{ Power }}" readonly>
                </div>
                <center>
                    <button type="submit" class="button">Submit</button>
                </center>
            </form>
        </div>
    </body>
</html>
```

css file 
```
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      
      body {
        font-family: 'Arial', sans-serif;
        background-color: #F0F7FA;
        color: #1a150e;
        display: flex;
        flex-direction:column;
        justify-content:flex-start;
        align-items: center;
        height: 100%;
        margin:10px;
      }
    
      hr {
        border-top: 2px solid black;
        margin: 20px 0;
        width: 100%;
    }
    
    p{
      margin:20px;
      font-size: 20;
    }
    
      .form-container {
        background:  #A0C9D6 ;
        border-radius: 10px;
        padding: 35px 30px;
        width: 750px;
        height: auto;
        display: flex;
        flex-direction:column;
        gap: 15px;
        margin-top: 3px;
      }
      
      .form-container h2 {
        font-size: 1.8rem;
        font-family: Georgia, 'Times New Roman', Times, serif;
        color: #4682b4;
        text-align: center;
      
      }
    
      .form-group {
        display: flex;
        flex-direction: column;
        gap: 5px;
      }
      
      .form-group label {
        font-size: 15px;
        color: #34495e;
        padding-top:15px;
        font-weight: bold;
      }
      .form-group input {
        padding: 15px;
        font-size: 1rem;
        border: 2px solid #bdc3c7;
        border-radius: 6px;
        background-color: #f8f9fa;
      }
      
      .form-group input:focus {
        border-color: #0077b6;
        box-shadow: 0 0 5px rgba(0, 119, 182, 0.5);
        outline: none;
      }
      
      .button-container {
        display: flex;
        justify-content: center;
      }
      
      .button {
        padding: 12px 30px;
        font-size: 1.1rem;
        font-weight: bold;
        background:#4682b4;
        color: white;
        border: none;
        margin-top: 20px;
        border-radius: 6px;
        cursor: pointer;
      }
      
      h1{
        padding-top: 10px;
        color:white;
        font-family: 'Times New Roman', Times, serif;
      }
      h2{
        padding-bottom: 10px;
        color:white;
      }
    
      .button:hover {
     
        background:lightblue;
        color:black;
        transform: scale(1.02);
      }
      /* Responsive Design */
      @media (max-width: 768px) {
        .form-container {
          width: 90%;
        }
        .form-group-container {
          grid-template-columns: 1fr;
        }
      }
    
    
</style>
```


## SERVER SIDE PROCESSING:
views.py
```
from django.shortcuts import render 
def findpower(request): 
    context={} 
    context['Power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistance','0')
        print('request=',request) 
        print('Intensity=',I) 
        print('Resistance=',R) 
        Power = int(I) * int(I)* int(R) 
        context['Power'] = Power 
        context['I'] = I
        context['R'] = R
        print('Power=',Power) 
    return render(request,'serverapp/mathserver.html',context)
```
urls.py 
```
from django.contrib import admin 
from django.urls import path 
from serverapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('mathserver/',views.findpower,name="mathserver"),
    path('',views.findpower,name="mathserverroot")
]
```


## HOMEPAGE:

![alt text](<ex5 output.png>)

![alt text](<ex5 terminal.png>)


## RESULT:
The program for performing server side processing is completed successfully.
