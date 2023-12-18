---
description: TKTKT
keywords: TKTKTKTK
layout: index.njk
---
Archives seem to have come into a kind of fashion as of late. In an age of existential precarity, they seem to offer solace in feeling knowable, certain, and grounding. The training procedures of AI foundation models like GPT have a close relationship with archives too, but instead need their accessibility, volume, and givenness, which allows archives to be composed and instrumentalized as training sets. Beyond the veil of nostalgia, a home to which one cannot return, this project presents a naive machine learning model alongside an informal archive of music from the early web. I developed this project during my residency at [Recurse Center](https://recurse.com) in the fall of 2023 to explore the fundamentals of each, and how they interact with each other.

The MIDI files collected here and used to train the model were once very new. In sifting through them, I've been searching for the feeling of technological transformation in an earlier age, how they unify the possibilties of new aesthetic experiences with the technics of producing and distributing this particular format of media. In both machine learning and the archive, there exist archetypes of transformation and conservation, containers for the hopes and fears about how we ourselves may change.

<!-- No one questions the _transformational_ quality of current state of the art in AI, but how do our fears and fantasies of this transformation align with the other kinds of transformations we routinely experience, when we shop for home goods or develop a crush on someone? -->
<!-- - This website is, in a sense, an archive of archives, the aggregation of many personal collections.  -->
<!-- - A closure around a set of possible aesthetic experiences aligned to the dream of technological transformation, of both the self and society. -->

### Technical notes
Before MP3s came to dominate how people would listen to music on the internet, the sounds of the early web ([and even BBS and Usenet before the world wide web](https://forums.theregister.com/forum/all/2019/07/12/a_pair_of_usenet_pirates_get_66_months_behind_bars/#:~:text=Usenet%2C%20that%20brings%20back%20memories.%20Used%20to%20use%20it%20when%20I%20started%20at%20Uni.%20Great%20source%20of%20mod%20and%20midi%20files%2Cnone%20of%20that%20new%20fangled%20MP3%20nonsence!)) were predominantly expressed via MIDI. 
Its tiny file-size was accomodated by bandwidth limitations of the 1980s and 90s, web-native support for the format came early from browsers like [Internet Explorer and Netscape Navigator](https://www.vice.com/en/article/a359xe/the-internets-first-hit-file-format-wasnt-the-mp3-it-was-midi#:~:text=In%20particular%2C%20Microsoft%E2%80%99s%20Internet%20Explorer%20supported%20it%20as%20far%20back%20as%20version%201.0%2C%20while%20Netscape%20Navigator%20supported%20it%20with%20the%20use%20of%20a%20plug%2Din%20and%20added%20native%20support%20starting%20in%20version%203.0.).

The neural net model used here is simple by design, and you can [check out and run the source code yourself right from your browser](https://colab.research.google.com/drive/1hpzG6ygsn0Cv44ImhyOn13eHtSo_Lccg#scrollTo=2KCKQ2kVr24C). My intent is to have the model be able to express something at once whimsical and general about the underlying archive, and to be simple enough to serve educational purposes. It does not represent the state of the art in 2023, nor is it intended to be used seriously as a tool for music creation. Furthermore, I planned for this model to be portable and cheap to run. In its current implementation, it exists as a ~800k parameter decoder-only transformer model that runs from an AWS Lambda Function every day around noon (GMT) to produce a piece of music around three minutes in length.

This project also owes a debt to [BitMIDI](https://bitmidi.com/about), which also developed the [MIDI player](https://github.com/feross/timidity) I've implemented on this site for your listening pleasure.

<!-- ### About
The MIDI Archive was borne out of an interest in the strange temporality of AI during my residency at [Recurse Center](https://recurse.com/) in the fall of 2023. Digital technological innovations of the last couple decades have come with increasingly polarized epistemologies, and current existential concerns around AGI, super-human AI, and agentic AI seem to carry both optimistic (accelerationist) and pessimistic (apocalytpic) fantasies of complete transformation of human civilization. But AI is as much a backwards-looking technology as it is forward, and this project aims to explore that paradox by developing a relatively naive neural net model along with an archive. -->

<!-- ### The Archive as Corpus (Training Dataset) -->
<!-- The recent development of foundation models has blurred the lines between the archive and the training set, with the distinction being perhaps more about the communities of people who rely on them. And while archives do have to answer to nuanced questions about the embedding and perpetuation of historical biases, this holds all the more true for those training foundation models. In the case of this model, I've been building the model and the archive alongside each other, with the model acting as a synthetic expression of the underlying archive, as a tool for sensemaking around an archive. -->

<!-- There's a blurriness between the archive and the training set in the age of machine learning, and much of the contentions around archives, like the perpetuation and reification of historical biases, hold ever more true for current foundational models built with the current state of the art in ML. This project is ultimately _not_ about replicating the early music web with AI, but instead about using AI as a tool for sensemaking around an archive. -->

<!-- That said, this archive has been assembled in a pretty whimsical way way, selecting for both the eccentric and the mundane. In some sense, it is also an archive of archives, as each collection that is featured here also represents the vision and curation of another human being, another node on the world wide web. -->

<!-- ### A brief history [1980 — 2000] -->
<!-- - 1980 | [Usenet launched](https://en.wikipedia.org/wiki/Usenet)
- 1983 | [The MIDI specification was first published](https://en.wikipedia.org/wiki/MIDI#:~:text=The%20MIDI%20specification%20was%20published,6%20and%20the%20Prophet%20600.)
- 1987 | [The MP3 format was developed](https://cs.stanford.edu/people/eroberts/cs201/projects/1999-00/dmca-2k/mp3.html#:~:text=MP3%2C%20or%20Motion%20Picture%20Expert,from%20the%20University%20of%20Erlangen.)
- 1994 | [GeoCities launched](https://en.wikipedia.org/wiki/GeoCities)
- 1999 | [Napster launched](https://en.wikipedia.org/wiki/Napster) -->

<!-- This website surfaces a small slice of this music culture on the early web, and exists as both an archive (a curated selection of MIDI files from various websites) and as a training corpus for a neural net, which produces a new piece of music every day around noon (GMT). You can listen to any file in the archive by clicking on it. This project also owes a debt to the [BitMIDI project](https://bitmidi.com/about), which also developed the [MIDI player](https://github.com/feross/timidity) I've implemented on this site. -->