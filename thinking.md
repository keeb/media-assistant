need to propagate root_path through so models have full context. I.e, Model.Album.Photos[x] gives me abs path to the actuall filesystem on disk

 -> should this be the responsibility of the loader (Azhdar?) or the Model itself?
  -> probably the loader so the models can stay simple..

  -> what data does a Picture then contain? A pointer to its location on disk? The actual bytes?


probably need to change Azhdar._albums into a dict {"name": "path"}

would be cool to auto detect image types.

also think about changing from, i.e, April 2022 to 04-2022

need to normalize file extension capitalization

need to remove the `#.` folder name shit