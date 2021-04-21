<map version="freeplane 1.8.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node TEXT="Maximizing the Spread of Influence through a Social Network" FOLDED="false" ID="ID_1490290984" CREATED="1617682523104" MODIFIED="1617682897204" STYLE="oval">
<font SIZE="18"/>
<hook NAME="MapStyle" zoom="1.614">
    <properties edgeColorConfiguration="#808080ff,#ff0000ff,#0000ffff,#00ff00ff,#ff00ffff,#00ffffff,#7c0000ff,#00007cff,#007c00ff,#7c007cff,#007c7cff,#7c7c00ff" fit_to_viewport="false"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt">
<font SIZE="24"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="fork">
<font NAME="SansSerif" SIZE="10" BOLD="false" ITALIC="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details"/>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes">
<font SIZE="9"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT"/>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
<cloud COLOR="#f0f0f0" SHAPE="ROUND_RECT"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="styles.topic" COLOR="#18898b" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subtopic" COLOR="#cc3300" STYLE="fork">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.subsubtopic" COLOR="#669900">
<font NAME="Liberation Sans" SIZE="10" BOLD="true"/>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" SHAPE_HORIZONTAL_MARGIN="10.0 pt" SHAPE_VERTICAL_MARGIN="10.0 pt">
<font SIZE="18"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,1" COLOR="#0033ff">
<font SIZE="16"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,2" COLOR="#00b439">
<font SIZE="14"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,3" COLOR="#990000">
<font SIZE="12"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,4" COLOR="#111111">
<font SIZE="10"/>
</stylenode>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,5"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,6"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,7"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,8"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,10"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level,11"/>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="AutomaticEdgeColor" COUNTER="9" RULE="ON_BRANCH_CREATION"/>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<node TEXT="Background" POSITION="right" ID="ID_1621431230" CREATED="1617682888179" MODIFIED="1617682906685">
<edge COLOR="#ff0000"/>
<node TEXT="Models for the processes by which ideas and influence propagate through a social network have been studied in a number of domains" ID="ID_140123078" CREATED="1617682943091" MODIFIED="1617682947582"/>
<node TEXT="Previous Work" ID="ID_1840372205" CREATED="1617682907348" MODIFIED="1617682951265">
<node TEXT="the diffusion of medical and technological innovations,&#xa;the sudden" ID="ID_111177382" CREATED="1617682961545" MODIFIED="1617682968023"/>
<node TEXT="and widespread adoption of various strategies in&#xa;game-theoretic settings" ID="ID_324429650" CREATED="1617682969347" MODIFIED="1617682974200"/>
<node TEXT="and the effects of “word of mouth” in the&#xa;promotion of new products." ID="ID_858316998" CREATED="1617682974423" MODIFIED="1617682981124"/>
</node>
</node>
<node TEXT="Fundamental Algorithmic Problem" POSITION="right" ID="ID_954248526" CREATED="1617682914285" MODIFIED="1617682936274">
<edge COLOR="#00ff00"/>
<node TEXT="if we can try to convince a subset of individuals to adopt a new product or innovation, and the goal is to trigger a large cascade of further adoptions, which set of individuals should we target?" ID="ID_919417052" CREATED="1617682991894" MODIFIED="1617682996453"/>
</node>
<node TEXT="Several Widely Studied Models" POSITION="right" ID="ID_161535543" CREATED="1617683027496" MODIFIED="1617683037622">
<edge COLOR="#ff00ff"/>
<node TEXT="We consider this problem in several of the most widely studied models in social network analysis" ID="ID_1247886683" CREATED="1617683067296" MODIFIED="1617683070160">
<node TEXT="\latex A social network as directed graph $G={E,V}$" ID="ID_555796965" CREATED="1618974398365" MODIFIED="1618974426362"/>
<node TEXT="Two Basic Diffusion Models" ID="ID_68145939" CREATED="1617683728190" MODIFIED="1617683735795">
<node TEXT="Basic assumption" ID="ID_1752279031" CREATED="1617683861135" MODIFIED="1617683873546">
<node TEXT="individual node&apos;s status" ID="ID_1811502722" CREATED="1617683812486" MODIFIED="1618974558411">
<node TEXT="active (adopter) or inactive" ID="ID_359016221" CREATED="1618974558413" MODIFIED="1618974559936"/>
</node>
<node TEXT="activeness tendency" ID="ID_1834838517" CREATED="1617683820778" MODIFIED="1618974562933">
<node TEXT="each node’s tendency to become active increases monotonically as more of its neighbors become active." ID="ID_925693519" CREATED="1618974562936" MODIFIED="1618974564235"/>
</node>
<node TEXT="status switch direction" ID="ID_8862280" CREATED="1617683833353" MODIFIED="1618974581331">
<node TEXT="nodes can switch from being inactive to being active, but do not switch in the other direction; it turns out that this assumption can easily be lifted later." ID="ID_1494142080" CREATED="1618974582209" MODIFIED="1618974583202"/>
</node>
</node>
<node TEXT="abstract procedure of influence spread" ID="ID_1700689529" CREATED="1618974599353" MODIFIED="1618974627939">
<node TEXT="\latex from an initially inactive node $v$, as time unfolds, more of $v$’s neighbors become active; at some point, this may cause $v$ to become active, and $v$’s decision may in turn trigger further decisions by nodes to which $v$ is connected." ID="ID_1099730519" CREATED="1618974637208" MODIFIED="1618974696518"/>
</node>
<node TEXT="Node-specific Threshold - Linear Threshold Model" ID="ID_1620434794" CREATED="1617683880141" MODIFIED="1617683894829">
<node TEXT="\latex influence weight $b_{v,w}$" ID="ID_607163516" CREATED="1618974858120" MODIFIED="1618974920862">
<node TEXT="\latex a node $v$ is influenced by $w \in N(v)$, her neighbor, according to a weight $b_{v,w}$ such that $\sum_{w \in N(v)} b_{v,w} \leq 1$" ID="ID_381915651" CREATED="1618974936944" MODIFIED="1618975096133"/>
</node>
<node TEXT="influence spread procedure" ID="ID_1769925032" CREATED="1618975108178" MODIFIED="1618975115842">
<node TEXT="\latex each node $v$ chooses a threshold $\theta_v \sim U[0,1]$, i.e., it represent the different latent tendencies&#xa; of nodes to adopt the innovation when their neighbors do and random draw is to show the lack of knowledge" ID="ID_740673924" CREATED="1618975117192" MODIFIED="1619020079395"/>
<node TEXT="\latex Given a random choice of thresholds, and an initial set of active nodes $A_0$ (with all other nodes inactive)," ID="ID_135033754" CREATED="1618975351591" MODIFIED="1618975382647"/>
<node TEXT="\latex in step $t$, all active nodes in step $t-1$ remain active, and we activate any&#xa;node $v$ for which the cumulative weight of her active neighbors is at least $\theta_v$, i.e., $\sum_{active \, w \in N(v)} b_{v,w} \geq \theta_{v}$" ID="ID_659818128" CREATED="1618975389128" MODIFIED="1618975651031"/>
</node>
</node>
<node TEXT="Dynamic Cascade Model - Independent Cascade Model" ID="ID_322896100" CREATED="1617684905591" MODIFIED="1617685022218">
<node TEXT="influence spread procedure" ID="ID_540801600" CREATED="1618975815433" MODIFIED="1618975838046">
<node TEXT="\latex Given an initial set of active nodes $A_0$ (with all other nodes inactive)," ID="ID_194235006" CREATED="1618975859869" MODIFIED="1618975870331"/>
<node TEXT="\latex When node $v$ first becomes active in step $t$, it is given a single chance to activate each currently inactive&#xa; neighbor $w$;" ID="ID_576479452" CREATED="1618975871927" MODIFIED="1619024071512">
<node TEXT="\latex it succeeds with a probability $p_{v,w}$, a parameter&#xa;of the system independently of the history" ID="ID_1331075037" CREATED="1618975938532" MODIFIED="1618976067818"/>
<node TEXT="\latex If $w$ has multiple newly activated neighbors, their attempts to activate $w$ are sequenced in an arbitrary order." ID="ID_1727033158" CREATED="1618976026240" MODIFIED="1618976096531"/>
<node TEXT="\latex If $v$ succeeds, then $w$ will become active in step $t+1$;" ID="ID_1600894594" CREATED="1618976030041" MODIFIED="1618976114419"/>
<node TEXT="\latex whether or not $v$ succeeds, it cannot make any further attempts to activate $w$ in subsequent rounds." ID="ID_1036461705" CREATED="1618976035728" MODIFIED="1618976131957"/>
</node>
<node TEXT="the process runs until no more activations are possible." ID="ID_813534963" CREATED="1618975944929" MODIFIED="1618975989421"/>
</node>
</node>
</node>
<node TEXT="Optimization Formulation" ID="ID_1538974125" CREATED="1618976454203" MODIFIED="1618976459379">
<node TEXT="\latex choosing a good initial set $A_0$ of nodes to start the diffusion process" ID="ID_998954994" CREATED="1618976471819" MODIFIED="1618976506254"/>
</node>
</node>
</node>
<node TEXT="NP-hard &amp; Approximiation Guarantee" POSITION="right" ID="ID_1832657275" CREATED="1617683040921" MODIFIED="1617683059934">
<edge COLOR="#00ffff"/>
<node TEXT="Section 2" ID="ID_1291895465" CREATED="1617686081660" MODIFIED="1617686097333"/>
<node TEXT="Problem Formulation" ID="ID_408531101" CREATED="1617685394389" MODIFIED="1617685409617">
<node TEXT="\latex influence of a set $A:\, \sigma(A)$" ID="ID_1022021288" CREATED="1617685411855" MODIFIED="1618976555519">
<node TEXT="\latex the expected number of active nodes at the end of the process, given $A$ as this initial active set $A_0$." ID="ID_159067256" CREATED="1618976571893" MODIFIED="1618976595703"/>
</node>
<node TEXT="influence maximization problem" ID="ID_1942434681" CREATED="1617685427139" MODIFIED="1617685442556">
<node TEXT="\latex for a parameter $k$, to find a $k$-node set of maximum influence." ID="ID_639951791" CREATED="1617685483168" MODIFIED="1618976635580"/>
</node>
</node>
<node TEXT="consider the issue of choosing influential sets of individuals as a problem in discrete optimization." ID="ID_1163825790" CREATED="1617683075967" MODIFIED="1617683423673">
<node TEXT="The optimization problem of selecting the most influential nodes is NP-hard here" ID="ID_1102404693" CREATED="1617683424642" MODIFIED="1617683425495"/>
</node>
<node TEXT="we provide the first provable approximation guarantees for efficient algorithms." ID="ID_1099807651" CREATED="1617683080459" MODIFIED="1617683088310">
<node TEXT="the optimal solution for influence maximization can be efficiently approximated to within a factor of (1-1/e-epsilon), in both the Linear Threshold and Independent Cascade models;" ID="ID_889435962" CREATED="1617685504342" MODIFIED="1617685527843"/>
<node TEXT="a generalization of the hill-climbing algorithm&#xa;still provides approximation guarantees arbitrarily close to (1 -1/e)." ID="ID_471519230" CREATED="1617685665713" MODIFIED="1617685672114"/>
</node>
</node>
<node TEXT="A Natural Greedy Algorithm" POSITION="right" ID="ID_101329813" CREATED="1617683061274" MODIFIED="1617683115742">
<edge COLOR="#7c0000"/>
<node TEXT="Overall Approach" ID="ID_294283032" CREATED="1618977042529" MODIFIED="1618977049619">
<node TEXT="sub-modular function" ID="ID_310601220" CREATED="1618977051209" MODIFIED="1618977058133">
<node TEXT="\latex Consider an arbitrary function $f(\cdot)$ that maps subsets of a finite set $U$ to non-negative real numbers" ID="ID_122941745" CREATED="1618977081095" MODIFIED="1618977121068"/>
<node TEXT="\latex $f$ is sub-modular if it satisfies a natural “diminishing&#xa;returns” property" ID="ID_547868956" CREATED="1618977124392" MODIFIED="1618977172020">
<node TEXT="\latex formally, a sub-modular function satisfies $f(S \cup \{v\}) - f(S) \geq f(T \cup \{v\}) - f(T)$, for all elements $v$ and all pairs of sets $S \subseteq T$." ID="ID_951215310" CREATED="1618977189754" MODIFIED="1618977274229"/>
<node TEXT="\latex the marginal gain from adding an element to a set $S$ is at least as high as the marginal gain from adding the same element to a superset of $S$" ID="ID_1495013516" CREATED="1618977153503" MODIFIED="1618977188981"/>
</node>
<node TEXT="one nice property" ID="ID_926211452" CREATED="1618977310628" MODIFIED="1618977316879">
<node TEXT="\latex Suppose we have a function f that is sub-modular, takes only nonnegative values, and is monotone: $f(S \cup \{v\})- f(S)$&#xa; for all elements $v$ and sets $S$." ID="ID_1458146333" CREATED="1618977343607" MODIFIED="1618977430338"/>
<node TEXT="\latex We wish to find a $k$-element set $S$ for which $f(S)$ is maximized." ID="ID_621446876" CREATED="1618977437692" MODIFIED="1618977451679"/>
<node TEXT="the following greedy hill-climbing algorithm approximates&#xa;the optimum to within a factor of (1 - 1/e)" ID="ID_735824540" CREATED="1618977363628" MODIFIED="1618977474558">
<node TEXT="start with the empty set, and repeatedly add an element that gives the maximum marginal gain." ID="ID_1264823678" CREATED="1618977475657" MODIFIED="1618977479743"/>
</node>
</node>
</node>
</node>
<node TEXT="Hill-climbing greedy algorithm THM2.1" ID="ID_1848214413" CREATED="1617686174385" MODIFIED="1617686195862">
<node TEXT="\latex For a non-negative, monotone sub-modular function $f$, let $S$ be a set of size $k$ obtained by selecting elements one at a time, each time choosing an element that provides the largest marginal increase in the function value. Let $S^*$ be a set that maximizes the value of $f$ over all $k$-element sets. Then $f(S) \geq (1-1/e) f(S^*)$,; in other words, S provides a (1-1/e)-approximation." ID="ID_1571655060" CREATED="1618977529581" MODIFIED="1618977614595"/>
</node>
<node TEXT="Our strategy" ID="ID_332359811" CREATED="1618977729940" MODIFIED="1618977751560">
<node TEXT="\latex show that for the models we are considering,&#xa;the resulting influence function \sigma(\cdot) is submodular" ID="ID_1160528722" CREATED="1618977751563" MODIFIED="1618977771142">
<node TEXT="\latex A subtle difficulty lies in the fact that the result of Nemhauser et al. assumes that the greedy algorithm can evaluate the underlying function exactly, which may not be the case for the influence function \sigma(A)" ID="ID_1646799546" CREATED="1618977818485" MODIFIED="1618977857889"/>
<node TEXT="\latex However, by simulating the diffusion process and sampling the resulting active sets, we are able to obtain arbitrarily close approximations to \sigma(A) with high probability" ID="ID_492799432" CREATED="1618977842529" MODIFIED="1618977876236"/>
<node TEXT="\latex for any $\epsilon &gt; 0$, there is $\gamma &gt;0$ such that by using $(1 + &#xd;\gamma)$-approximate values for the&#xa;function to be optimized, we obtain a $(1-1/e-\epsilon)$-approximation." ID="ID_982208811" CREATED="1618977877339" MODIFIED="1618977941419"/>
</node>
<node TEXT="Dynamic Cascade Model - Independent Cascade Model" ID="ID_979915581" CREATED="1617684905591" MODIFIED="1617685022218">
<node TEXT="THM 2.2 show the influence function is sub-modular" ID="ID_1133134079" CREATED="1618978266205" MODIFIED="1618978319357">
<node TEXT="proof in p4" ID="ID_1481133161" CREATED="1618978319553" MODIFIED="1618978326206"/>
</node>
<node TEXT="CLM 2.3" ID="ID_370067737" CREATED="1618978387053" MODIFIED="1618978390930"/>
<node TEXT="THM 2.4 NP-hard" ID="ID_647110942" CREATED="1618978334479" MODIFIED="1618978350230"/>
</node>
<node TEXT="Node-specific Threshold - Linear Threshold Model" ID="ID_599635535" CREATED="1617683880141" MODIFIED="1617683894829">
<node TEXT="THM 2.5 show the influence function is sub-modular" ID="ID_1854406887" CREATED="1618978266205" MODIFIED="1618978366654">
<node TEXT="proof in p4" ID="ID_1221387094" CREATED="1618978319553" MODIFIED="1618978326206"/>
</node>
<node TEXT="CLM 2.6" ID="ID_989583939" CREATED="1618978394016" MODIFIED="1618978397241"/>
<node TEXT="THM 2.7 NP-hard" ID="ID_855813494" CREATED="1618978334479" MODIFIED="1618978424092"/>
</node>
</node>
<node TEXT="Extensions" ID="ID_731387366" CREATED="1618978121478" MODIFIED="1618978130204">
<node TEXT="p3 - complex marketing actions" ID="ID_1538673666" CREATED="1618978131094" MODIFIED="1618978145744"/>
<node TEXT="p3 - non-negative weight" ID="ID_974847158" CREATED="1618978133978" MODIFIED="1618978155957"/>
</node>
</node>
<node TEXT="Computational Experiments" POSITION="right" ID="ID_317568029" CREATED="1617683206195" MODIFIED="1617683221387">
<edge COLOR="#00007c"/>
<node TEXT="Datasets - Network" ID="ID_290729786" CREATED="1617686222666" MODIFIED="1618978564969">
<node TEXT="a collaboration graph obtained from co-authorships in physics publications, with simple settings of the influence parameters. e-print arXiv" ID="ID_1059932031" CREATED="1618978690145" MODIFIED="1618978701487"/>
<node TEXT="https://snap.stanford.edu/data/ca-HepPh.html" ID="ID_577919978" CREATED="1618978959442" MODIFIED="1618978960361"/>
<node TEXT="preprocess" ID="ID_673267579" CREATED="1618978748691" MODIFIED="1618978752093">
<node TEXT="The collaboration graph contains a node for each researcher who&#xa;has at least one paper with co-author(s) in the arXiv database. For each paper with two or more authors, we inserted an edge for each pair of authors (single-author papers were ignored). Notice that this results in parallel edges when two researchers have co-authored multiple papers — we kept these parallel edges as they can be interpreted to indicate stronger social ties between the researchers involved. The resulting graph has 10748 nodes, and edges between about 53000 pairs of nodes." ID="ID_179486826" CREATED="1618978753383" MODIFIED="1618978775480"/>
</node>
</node>
<node TEXT="Proposed Greedy Method" ID="ID_282149312" CREATED="1618978537916" MODIFIED="1618978634429">
<node TEXT="In the linear threshold model, we treated the multiplicity of edges as weights." ID="ID_1753550220" CREATED="1618980097189" MODIFIED="1618980155578"/>
<node TEXT="In the independent cascade model, we assigned a uniform probability of p to each edge of the graph, choosing p to be 1% and 10% in separate trials." ID="ID_712983689" CREATED="1618980280323" MODIFIED="1618980305725"/>
<node TEXT="a special case of the Independent Cascade Model that we term “weighted cascade”" ID="ID_37047029" CREATED="1618980369536" MODIFIED="1618980372726"/>
</node>
<node TEXT="baselines" ID="ID_1070705485" CREATED="1618978566391" MODIFIED="1618980394078">
<node TEXT="high-degree heuristic" ID="ID_55056940" CREATED="1618980395102" MODIFIED="1618980410163"/>
<node TEXT="distance-centrality" ID="ID_1839476851" CREATED="1618980410336" MODIFIED="1618981068328"/>
<node TEXT="uniformly draw" ID="ID_645552789" CREATED="1618981068626" MODIFIED="1618981079003"/>
</node>
<node TEXT="Results show that, in addition to their provable guarantees,&#xa;our approximation algorithms significantly out-perform node-selection heuristics based on the well-studied notions of degree centrality and distance centrality from the field of social networks." ID="ID_1574956978" CREATED="1617683240588" MODIFIED="1617686221488"/>
<node TEXT="we describe in Section 3 the results of computational experiments with both the Linear Threshold and Independent Cascade Models, showing that the hill-climbing algorithm significantly out-performs strategies based on targeting high-degree or “central” nodes" ID="ID_1623560288" CREATED="1617685834050" MODIFIED="1617685843114"/>
</node>
<node TEXT="A General Model of Diffusion Process" POSITION="right" ID="ID_1087037853" CREATED="1617685771450" MODIFIED="1617685863852">
<edge COLOR="#007c00"/>
<node TEXT="we then develop a general model of diffusion processes in social networks that simultaneously generalizes the Linear Threshold and Independent Cascade Models, as well as a number of other natural cases" ID="ID_1684876519" CREATED="1617685877391" MODIFIED="1617685897775"/>
<node TEXT="and we show how to obtain approximation guarantees for a large sub-class of these models" ID="ID_1529366665" CREATED="1617685898186" MODIFIED="1617685903252"/>
</node>
<node TEXT="Extensions" POSITION="right" ID="ID_1441479949" CREATED="1617685806849" MODIFIED="1617685915445">
<edge COLOR="#7c007c"/>
<node TEXT="more complex marketing actions" ID="ID_1233174445" CREATED="1617685915447" MODIFIED="1617686012575">
<node TEXT="we may have a number m of different marketing&#xa;actions Mi available, each of which may affect some subset of nodes by increasing their probabilities of becoming active, without necessarily making them active deterministically." ID="ID_1245076587" CREATED="1617687151143" MODIFIED="1617687162461"/>
<node TEXT="The more we spend on any one action the stronger its effect will be; however, different nodes may respond to marketing actions in different ways" ID="ID_1872199613" CREATED="1617687163010" MODIFIED="1617687167402"/>
</node>
<node TEXT="non-progressive processes" ID="ID_1052825708" CREATED="1617686015448" MODIFIED="1617686024891">
<node TEXT="in which active nodes may become inactive in subsequent steps" ID="ID_1347546226" CREATED="1617686025989" MODIFIED="1617686030093"/>
</node>
</node>
</node>
</map>
