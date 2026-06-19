
#include <bits/stdc++.h>
using namespace std;

// ── Macros ────────────────────────────────
#define int long long
#define pb push_back
#define eb emplace_back
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) (int)(x).size()
#define fi first
#define se second

// ── Types ───────────────────────────────────
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;

// ── Constants ────────────────────────────────
const int MOD = 1e9 + 7;
const int INF = 1e18;

// ── Fast I/O ──────────────────────────────────
void fastio()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
}

// ── Modular Arithmetic ────────────────────────────
int mod_pow(int base, int exp, int mod = MOD)
{
    int res = 1;
    base %= mod;
    while (exp)
    {
        if (exp & 1)
            res = res * base % mod;
        base = base * base % mod;
        exp >>= 1;
    }
    return res;
}

int mod_inv(int a, int mod = MOD)
{
    return mod_pow(a, mod - 2, mod);
}

// ── DSU (Disjoint Set Union) ───────────────────────
struct DSU {
    vector<int> parent, size;

    DSU(int n) {
        parent.resize(n + 1);
        size.assign(n + 1, 1); // each node is its own component (size = 1)
        iota(parent.begin(), parent.end(), 0); // parent[x] = x (root)
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]); // path compression (flatten tree)
    }

    bool unite(int a, int b) {
        a = find(a); // find root of a
        b = find(b); // find root of b
        if (a == b) return false; // already same component

        if (size[a] < size[b]) swap(a, b); // attach smaller tree under larger
        parent[b] = a; // make a the parent (root)
        size[a] += size[b]; // update size of new root

        return true;
    }
};

// ── Binary Search Helpers ─────────────────────────
int lower_idx(vi &arr, int val)
{
    return lower_bound(all(arr), val) - arr.begin();
}

int upper_idx(vi &arr, int val)
{
    return upper_bound(all(arr), val) - arr.begin();
}

// ── Prefix Sum 2D ────────────────────────────────
vvi build_prefix(vvi &a, int n, int m)
{
    vvi prefix(n + 1, vi(m + 1, 0));
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            prefix[i][j] = a[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
        }
    }
    return prefix;
}

int query_prefix(vvi &p, int r1, int c1, int r2, int c2)
{
    return p[r2][c2] - p[r1 - 1][c2] - p[r2][c1 - 1] + p[r1 - 1][c1 - 1];
}

// ── Dijkstra ────────────────────────────────────
vi dijkstra(int n, vector<vpii> &adj, int src)
{
    vi dist(n + 1, INF);
    priority_queue<pii, vpii, greater<>> pq;

    dist[src] = 0;
    pq.push({0, src});

    while (!pq.empty())
    {
        auto [d, u] = pq.top();
        pq.pop();
        if (d > dist[u])
            continue;

        for (auto [v, w] : adj[u])
        {
            if (dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

// ── Solve Function ────────────────────────────────
void solve()
{
}

// ── Main ──────────────────────────────────────
signed main()
{
    fastio();
    int t = 1;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
