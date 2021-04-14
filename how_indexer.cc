==============================================================================

in
~/sluha/indexer/test-service/bin

indexer.py
Uwsgi mule runs nonstop and accepts messages from workers.
When data for worker is ready, mule sends him signal and worker cand read the data.
==============================================================================
IndexerWrapper

include
Stores running indexer processes or their return values. Key is idn.
IndexerWrapper.idns = {}


    try:
               output = os.path.join(self.output_path, str(idn))
 W>            proc = subprocess.Popen(['./worker',
 W>                                  '-i', str(idn),
 W>                                  '-f', self.worker_conf,
 W>                                  '-t', job_path + ':' + output],
 W>                                  cwd = self.indexer_path,
 W>                                  stdout = subprocess.DEVNULL,
 W>                                  stderr = subprocess.DEVNULL)
IndexerWrapper.idns[str(idn)] = proc
it starts worker processes and store it in idns list
:x!
==============================================================================





==============================================================================
in srv.py
flask rest API server
in test_download_async
post is synchronized using
   uwsgi.mule_msg(json.dumps(msg), 0)

uwsgi.mule_msg(json.dumps(msg), 0)
#Must wait for response from mule, so that we know if metadata are ready.
uwsgi.signal_wait(uwsgi.worker_id())
==============================================================================
class ParserContext_t {
   public:
       enum EncodingSource_t {
           ENCODING_SOURCE_HEADER,
           ENCODING_SOURCE_DETECTED,
           ENCODING_SOURCE_META
       };

       szn::indexer::TreeBuilder *treeBuilder;
       std::string charset;
       EncodingSource_t charsetSource;
       hubbub_tree_handler tree_handler;
       hubbub_parser *parser;

       ParserContext_t(const std::string &charset, hubbub_parser *parser, szn::indexer::TreeBuilder *treeBuilder):
           treeBuilder(treeBuilder),
           charset(charset),
           charsetSource(ENCODING_SOURCE_HEADER),
           tree_handler(parser_tree_handler),
           parser(parser)
       {
           tree_handler.ctx = (void *) this;
       }
   };

============================================================================== 
/* Prototype tree handler struct */
   static hubbub_tree_handler parser_tree_handler = {
       create_comment,
       create_doctype,
       create_element,
       create_text,
       ref_node,
       unref_node,
       append_child,
       insert_before,
       remove_child,
       clone_node,
       reparent_children,
       get_parent,
       has_children,
       form_associate,
       add_attributes,
       set_quirks_mode,
       change_encoding,
       script_complete,
       NULL
   };
   
============================================================================== 



