using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace AdventOfCode2017
{
  class Day12
  {
    private const string INPUT_PATTERN = @"^(\d+) <-> ((\d+)(, \d+)*)$";
    private const int PROGRAM_INDEX = 1;
    private const int CONNECTED_PROGRAMS_INDEX = 2;

    public static void Main(string[] args)
    {
      var input = new string[]
      {
        "0 <-> 2",
        "1 <-> 1",
        "2 <-> 0, 3, 4",
        "3 <-> 2, 4",
        "4 <-> 2, 3, 6",
        "5 <-> 6",
        "6 <-> 4, 5"
      };

      Console.WriteLine(FindNumConnections(input, 0));

      Console.WriteLine(FindNumConnections(Util.GetFileLines("Day12"), 0));

      Console.WriteLine(FindNumGroups(input));

      Console.WriteLine(FindNumGroups(Util.GetFileLines("Day12")));

      Console.ReadKey();
    }

    private static int FindNumGroups(string[] input)
    {
      int numGroups = 0;

      Dictionary<int, Node> nodes = ConstructNodes(input);

      Dictionary<int, HashSet<int>> groups = new Dictionary<int, HashSet<int>>();

      foreach (KeyValuePair<int, Node> idToNode in nodes)
      {
        bool nodeAlreadyInGroup = false;

        foreach (KeyValuePair<int, HashSet<int>> groupIdToNodes in groups)
        {
          if (groupIdToNodes.Value.Contains(idToNode.Key))
          {
            nodeAlreadyInGroup = true;
            break;
          }
        }

        if (!nodeAlreadyInGroup)
        {
          groups[numGroups++] = FindConnections(nodes, idToNode.Key);
        }
      }

      return numGroups;
    }

    private static int FindNumConnections(string[] input, int root)
    {
      Dictionary<int, Node> nodes = ConstructNodes(input);
      return FindConnections(nodes, root).Count;
    }

    private static HashSet<int> FindConnections(Dictionary<int, Node> nodes, int root)
    {
      Node rootNode = nodes[root];
      HashSet<int> connections = new HashSet<int>();
      Queue<Node> nodesToCheck = new Queue<Node>();
      nodesToCheck.Enqueue(rootNode);

      while (nodesToCheck.Count > 0)
      {
        Node nodeToCheck = nodesToCheck.Dequeue();
        if (!connections.Add(nodeToCheck.id))
        {
          continue;
        }

        foreach (Node neighbour in nodeToCheck.neighbours)
        {
          nodesToCheck.Enqueue(neighbour);
        }
      }

      return connections;
    }

    private static Dictionary<int, Node> ConstructNodes(string[] input)
    {
      Dictionary<int, Node> nodes = new Dictionary<int, Node>();

      foreach(string i in input)
      {
        Regex rgx = new Regex(INPUT_PATTERN);

        Match match = rgx.Match(i);

        int id = int.Parse(match.Groups[PROGRAM_INDEX].Value);

        Node node = new Node(id);

        IEnumerable<int> neighbours = FindNeighbours(i);

        foreach (int neighbour in neighbours)
        {
          if (nodes.ContainsKey(neighbour))
          {
            nodes[neighbour].AddNeighbour(node);
            node.AddNeighbour(nodes[neighbour]);
          }
        }

        nodes[id] = node;
      }

      return nodes;
    }

    private static IEnumerable<int> FindNeighbours(string input)
    {
      Regex rgx = new Regex(INPUT_PATTERN);

      Match match = rgx.Match(input);

      return match.Groups[CONNECTED_PROGRAMS_INDEX].Value
        .Split(new[] { ", " }, StringSplitOptions.RemoveEmptyEntries)
        .Select(n => int.Parse(n));
    }

    private class Node
    {
      public readonly int id;
      public List<Node> neighbours;

      public Node(int id)
      {
        this.id = id;
        this.neighbours = new List<Node>();
      }

      public void AddNeighbour(Node node)
      {
        this.neighbours.Add(node);
      }
    }
  }
}
