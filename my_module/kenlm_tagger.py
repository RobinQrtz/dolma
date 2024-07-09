from dolma.core.data_types import DocResult, Document, Span
from dolma.core.registry import TaggerRegistry
from dolma.core.taggers import BaseTagger

import kenlm  # type: ignore
import sentencepiece  # type: ignore
import text_normalizer


def pp(log_score, length):
    return 10.0 ** (-log_score / length)


class KenLMTaggerBase(BaseTagger):
    def __init__(
        self, kenlm_fn, spiece_fn, load_method: int = 2, normalize: bool = False
    ):
        self.normalize = normalize
        self.lm_config = kenlm.Config()
        # This is the default settings
        # POPULATE will mmap the models and populate the pages.
        # Maybe that's not the best way when the models are on a network disk.
        # TODO: try copying models file, try READ or PARALLEL_READ
        self.lm_config.load_method = load_method
        self.kenlm_model = kenlm.Model(kenlm_fn, self.lm_config)

        self.spiece_model = sentencepiece.SentencePieceProcessor()
        self.spiece_model.load(spiece_fn)

    def predict(self, doc: Document) -> DocResult:
        tokenized = " ".join(self.spiece_model.encode_as_pieces(doc.text))
        doc_log_score, doc_length = 0, 0
        for line in tokenized:
            if self.normalize:
                line = text_normalizer.normalize(line)
            log_score = self.kenlm_model.score(line)
            length = len(line.split()) + 1
            doc_log_score += log_score
            doc_length += length

        score = round(pp(doc_log_score, doc_length), 1)
        return DocResult(
            doc=doc,
            spans=[Span(start=0, end=len(doc.text), type="kenlm_score", score=score)],
        )


@TaggerRegistry.add("kenlm_swedish")
class KenLMTaggerSwedish(KenLMTaggerBase):
    def __init__(self):
        pass
        # self.super.__init__(kenlm_path, spiece_fn_pat)
