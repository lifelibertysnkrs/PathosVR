using UnityEngine;
using System;
using System.IO;
using System.Collections.Generic;
using System.Diagnostics;
public class sinx : MonoBehaviour
{

    // Definitions

    public float growTimer = 0;
    private List<float> Months = new List<float>();
    private List<float> Deaths = new List<float>();
    private String dataFile = "test.csv";
    private int iterator = 0;
    private float totalDeaths;


    // Use this for initialization
    void Start()
    {
      
    }

    // Update is called once per frame
    void Update()
    {
        //Gets time
        growTimer += (float)Time.deltaTime;

        //creates variables

        int currentmonth = (int)Months[iterator]; 
        int newdeaths = (int)Deaths[iterator]; //New deaths per month
        totalDeaths += (int)Deaths[iterator]; //Total deaths from beginning
        

        //Move things around
        //
        //
        //
        //
        //



        //iterates
        iterator++;
        
    }

    void getData() //Reads data from CSV file
    {

    var reader = new StreamReader(File.OpenRead(@"test.csv"));


    while (!reader.EndOfStream)
        {
        var line = reader.ReadLine();
        var values = line.Split(',');

        Months.Add(Convert.ToSingle(values[0]));
        Deaths.Add(Convert.ToSingle(values[1]));
        }
    }
  
}
    

