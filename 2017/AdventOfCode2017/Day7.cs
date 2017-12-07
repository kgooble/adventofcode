using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace AdventOfCode2017
{
  class Day7
  {
    public static void Main(string[] args)
    {
      string[] testInput = new[]
      {
        "pbga (66)",
        "xhth (57)",
        "ebii (61)",
        "havc (66)",
        "ktlj (57)",
        "fwft (72) -> ktlj, cntj, xhth",
        "qoyq (66)",
        "padx (45) -> pbga, havc, qoyq",
        "tknk (41) -> ugml, padx, fwft",
        "jptl (61)",
        "ugml (68) -> gyxo, ebii, jptl",
        "gyxo (61)",
        "cntj (57)"
      };

      Util.CheckAnswer(testInput, FindBottomProgram, "tknk");

      Part1();

      Util.CheckAnswer(testInput, FindIdealWeight, 60);

      Part2();

      Console.ReadKey();
    }

    private static void Part1()
    {
      Console.WriteLine(FindBottomProgram(Util.GetFileLines("Day7")));
    }

    private static void Part2()
    {
      Console.WriteLine(FindIdealWeight(Util.GetFileLines("Day7")));
    }

    private static string FindBottomProgram(string[] programInputs)
    {
      List<Program> programs = CreatePrograms(programInputs);
      return FindRoot(programs)?.name;
    }

    private static int FindIdealWeight(string[] programInputs)
    {
      List<Program> programs = CreatePrograms(programInputs);

      Program root = FindRoot(programs);

      var queue = new Queue<Program>();
      queue.Enqueue(root);

      Program unevenChild = null;

      while (queue.Count > 0)
      {
        Program parent = queue.Dequeue();

        if (parent.children.Count == 0)
        {
          continue;
        }

        unevenChild = FindUnevenChild(parent);

        if (unevenChild == null)
        {
          parent.children.ForEach(child => queue.Enqueue(child));
        }
        else
        {
          break;
        }
      }

      while (true)
      {
        Program nextUnevenChild = FindUnevenChild(unevenChild);

        if (nextUnevenChild == null)
        {
          List<int> weights = new List<int>(unevenChild.parent.children.Select(child => child.TotalWeight));
          ISet<int> weightSet = new HashSet<int>(weights);
          Dictionary<int, int> weightToCount = weights.GroupBy(weight => weight).ToDictionary(group => group.Key, group => group.Count());
          int unevenWeight = weightToCount[weightSet.First()] > 1 ? weightSet.Where(w => w != weightSet.First()).First() : weightSet.First();
          int evenWeight = weights.Where(w => w != unevenWeight).First();

          return unevenChild.weight + (evenWeight - unevenWeight);
        }

        unevenChild = nextUnevenChild;
      }
    }

    private static Program FindUnevenChild(Program parent)
    {
      List<int> weights = new List<int>(parent.children.Select(child => child.TotalWeight));
      ISet<int> weightSet = new HashSet<int>(weights);
      if (weightSet.Count > 1)
      {
        Dictionary<int, int> weightToCount = weights.GroupBy(weight => weight).ToDictionary(group => group.Key, group => group.Count());
        int unevenWeight = weightToCount[weightSet.First()] > 1 ? weightSet.Where(w => w != weightSet.First()).First() : weightSet.First();
        return parent.children.Find(child => child.TotalWeight == unevenWeight);
      }

      return null;
    }

    private static Program FindRoot(List<Program> programs)
    {
      foreach (Program program in programs)
      {
        if (program.parent == null)
        {
          return program;
        }
      }

      return null;
    }

    private static List<Program> CreatePrograms(string[] programInputs)
    {
      var programs = new List<Program>();

      foreach (string input in programInputs)
      {
        Program newProgram = FindOrCreateProgram(programs, input);

        foreach (string child in GetChildNames(input))
        {
          Program potentialChild = programs.Find(p => p.name == child);

          if (potentialChild == null)
          {
            potentialChild = new Program(child, newProgram);
            programs.Add(potentialChild);
          }
          else
          {
            potentialChild.SetParent(newProgram);
          }

          newProgram.AddChild(potentialChild);
        }
      }

      return programs;
    }

    private static Program FindOrCreateProgram(List<Program> existingPrograms, string input)
    {
      Program newProgram = CreateProgram(input);
      Program existingProgram = existingPrograms.Find(p => p.name == newProgram.name);

      if (existingProgram == null)
      {
        existingPrograms.Add(newProgram);
        return newProgram;
      }

      existingProgram.SetWeight(newProgram.weight);
      return existingProgram;
    }

    private static Program CreateProgram(string input)
    {
      string[] parts = input.Split(new[] { " -> " }, StringSplitOptions.RemoveEmptyEntries);

      string[] nameAndWeight = parts[0].Split(' ');

      string name = nameAndWeight[0];
      int weight = int.Parse(nameAndWeight[1].Substring(1, nameAndWeight[1].Length - 2));

      return new Program(name, weight);
    }

    private static IEnumerable<string> GetChildNames(string input)
    {
      string[] parts = input.Split(new[] { " -> " }, StringSplitOptions.RemoveEmptyEntries);

      if (parts.Length == 1)
      {
        return new string[0];
      }

      return parts[1].Split(new[] { ", " }, StringSplitOptions.RemoveEmptyEntries);
    }

    private class Program
    {
      public string name;
      public int weight;
      public Program parent;
      public List<Program> children = new List<Program>();

      private int? totalWeight;

      public Program(string name, int weight)
      {
        this.name = name;
        this.weight = weight;
      }

      public Program(string name, Program parent)
      {
        this.name = name;
        this.parent = parent;
      }

      public int TotalWeight
      {
        get
        {
          if (this.totalWeight == null)
          {
            this.totalWeight = this.weight + this.children.Sum(child => child.TotalWeight);
          }

          return this.totalWeight.Value;
        }
      }

      public void SetWeight(int weight)
      {
        this.weight = weight;
      }

      public void SetParent(Program parent)
      {
        this.parent = parent;
      }

      public void AddChild(Program child)
      {
        this.children.Add(child);
      }
    }
  }
}
