int dumpWordBarrel( std::stringstream &stream, 
std::string file, 
uint64_t wordId, 
uint64_t documentId, 
const DocumentBarrel_t& docBarrel, 
const std::map<WordHash_t, 
std::string>& hash2word) 
{                                                                                                     
    BarrelDirReader_t<WordBarrelReader_t, WordRecord_t> wbr;
    if (wbr.open(file) != 0) return 1;
    for (; !wbr.eof(); wbr.readNext()) {
    if (wordId != 0 && wordId != wbr.getId()) {
    continue;
}
   wbr.dump(stream);                                                     
