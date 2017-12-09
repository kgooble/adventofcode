using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace AdventOfCode2017
{
  class Day9
  {
    public static void Main(string[] args)
    {
      Util.CheckAnswer("{}", CalculateScore, 1);
      Util.CheckAnswer("{{{}}}", CalculateScore, 6);
      Util.CheckAnswer("{{},{}}", CalculateScore, 5);
      Util.CheckAnswer("{{{},{},{{}}}}", CalculateScore, 16);
      Util.CheckAnswer("{<a>,<a>,<a>,<a>}", CalculateScore, 1);
      Util.CheckAnswer("{{<ab>},{<ab>},{<ab>},{<ab>}}", CalculateScore, 9);
      Util.CheckAnswer("{{<!!>},{<!!>},{<!!>},{<!!>}}", CalculateScore, 9);
      Util.CheckAnswer("{{<a!>},{<a!>},{<a!>},{<ab>}}", CalculateScore, 3);

      Util.PrintOutputFromFile<string, int>("Day9", CalculateScore);

      Util.CheckAnswer("{<>}", CountGarbage, 0);
      Util.CheckAnswer("{<random characters>}", CountGarbage, 17);
      Util.CheckAnswer("{<<<<>}", CountGarbage, 3);
      Util.CheckAnswer("{<{!>}>}", CountGarbage, 2);
      Util.CheckAnswer("{<!!>}", CountGarbage, 0);
      Util.CheckAnswer("{<!!!>>}", CountGarbage, 0);
      Util.CheckAnswer("{<{o\"i!a,<{i<a>}", CountGarbage, 10);

      Util.PrintOutputFromFile<string, int>("Day9", CountGarbage);

      Console.ReadKey();
    }

    private static int CalculateScore(string input)
    {
      var parser = new Parser();

      Group group = parser.Parse(input);

      return group.CalculateScore();
    }

    private static int CountGarbage(string input)
    {
      var parser = new Parser();

      Group group = parser.Parse(input);

      return group.CountGarbage();
    }
  }

  abstract class Content
  {
    public abstract int CalculateScore(int initial = 0);

    public abstract int CountGarbage();
  }

  class Group : Content
  {
    public readonly Group parent;
    public List<Content> children = new List<Content>();

    public Group(Group parent = null)
    {
      this.parent = parent;
    }

    public void AddChild(Content content)
    {
      this.children.Add(content);
    }

    public override int CalculateScore(int initial = 1)
    {
      return initial + this.children.Sum(c => c.CalculateScore(initial + 1));
    }

    public override int CountGarbage()
    {
      return this.children.Sum(c => c.CountGarbage());
    }
  }

  class Garbage : Content
  {
    private StringBuilder text = new StringBuilder();

    public Garbage(char c)
    {
      this.text.Append(c);
    }

    public void Append(char c)
    {
      this.text.Append(c);
    }

    public override int CalculateScore(int initial = 0)
    {
      return 0;
    }

    public override int CountGarbage()
    {
      return this.text.Length - 2;
    }
  }

  class Parser
  {
    public Group Parse(string input)
    {
      Group currentGroup = null;
      Garbage currentGarbage = null;

      for (int i = 0; i < input.Length; i++)
      {
        char c = input[i];

        if (currentGroup == null && currentGarbage == null)
        {
          if (c == '{')
          {
            currentGroup = new Group();
          }
          else if (c == ',')
          {
            // skip
          }
          else
          {
            throw new ArgumentException($"Ran into unexpected character {c} without group or garbage");
          }
        }
        else if (currentGarbage != null)
        {
          if (c == '!')
          {
            i += 1;
          }
          else if (c == '>')
          {
            currentGarbage.Append(c);
            currentGarbage = null;
          }
          else
          {
            currentGarbage.Append(c);
          }
        }
        else
        {
          if (c == '{')
          {
            Group newGroup = new Group(currentGroup);
            currentGroup.AddChild(newGroup);
            currentGroup = newGroup;
          }
          else if (c == '}')
          {
            if (currentGroup.parent == null)
            {
              return currentGroup;
            }

            currentGroup = currentGroup.parent;
          }
          else if (c == '<')
          {
            currentGarbage = new Garbage(c);
            currentGroup.AddChild(currentGarbage);
          }
        }
      }

      return currentGroup;
    }
  }
}
