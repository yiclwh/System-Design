# quick select top K

def getTopK(nums, K):
    selectTopK(nums, K, 0, len(nums)-1)
    return nums[:K]

def selectTopK(nums, K, start, end):
    if not nums or len(nums) <= K:
        return nums
    i = j = start
    p = nums[end]
    while i < end:
        if nums[i] < p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            i += 1
    nums[j], num[end] = nums[end], nums[j]
    length = j- start + 1
    if length == K:
        return
    elif length < K:
        getTopK(nums, K-length, j + 1, end)
    else:
        getTopK(nums, K, start, j - 1)

"""
Find top k frequent words with map reduce framework.

The mapper's key is the document id, value is the content of the document, words in a document are split by spaces.

For reducer, the output should be at most k key-value pairs, which are the top k words and their frequencies in this reducer. 
The judge will take care about how to merge different reducers' results to get the global top k frequent words, so you don't need to care about that part.

The k is given in the constructor of TopK class.

Given document A =
    lintcode is the best online judge
    I love lintcode

and document B =
    lintcode is an online judge for coding interview
    you can test your code online at lintcode

The top 2 words and their frequencies should be
lintcode, 4
online, 3

使用map reduce框架查找最常使用的k个单词.
mapper的key为文档的id, 值是文档的内容, 文档中的单词由空格分割.
对于reducer，应该输出最多为k个key-value对, 包括最常用的k个单词以及他们在当前reducer中的使用频率.
评判系统会合并不同的reducer中的结果以得到 全局 最常使用的k个单词, 所以你不需要关注这一环节. k 在TopK类的构造器中给出.

"""

/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */
class Pair {
    String key;
    int value;
    
    Pair(String key, int value) {
        this.key = key;
        this.value = value;
    }
}

public class TopKFrequentWords {

    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Write your code here
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);
            int id = value.id;
            String content = value.content;
            String[] words = content.split(" ");
            for (String word : words)
                if (word.length() > 0) {
                    output.collect(word, 1);
                }
        }
    }

    public static class Reduce {
        private PriorityQueue<Pair> Q = null;
        private int k;

        private Comparator<Pair> pairComparator = new Comparator<Pair>() {
            public int compare(Pair left, Pair right) {
                if (left.value != right.value) {
                    return left.value - right.value;
                }
                return right.key.compareTo(left.key);
            }
        };

        public void setup(int k) {
            // initialize your data structure here
            this.k = k;
            Q = new PriorityQueue<Pair>(k, pairComparator);
        }   

        public void reduce(String key, Iterator<Integer> values) {
            // Write your code here
            int sum = 0;
            while (values.hasNext()) {
                    sum += values.next();
            }

            Pair pair = new Pair(key, sum);
            if (Q.size() < k) {
                Q.add(pair);
            } else {
                Pair peak = Q.peek();
                if (pairComparator.compare(pair, peak) > 0) {
                    Q.poll();
                    Q.add(pair);
                }
            }
        }

        public void cleanup(OutputCollector<String, Integer> output) {
            // Output the top k pairs <word, times> into output buffer.
            // Ps. output.collect(String key, Integer value);
            List<Pair> pairs = new ArrayList<Pair>();
            while (!Q.isEmpty()) {
                pairs.add(Q.poll());
            }

            // reverse result
            int n = pairs.size();
            for (int i = n - 1; i >= 0; --i) {
                Pair pair = pairs.get(i);
                output.collect(pair.key, pair.value);
            }
        }
    }