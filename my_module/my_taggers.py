from dolma.core.data_types import DocResult, Document
from dolma.core.registry import TaggerRegistry
from dolma.core.taggers import BaseTagger
from dolma.taggers.gopher import get_attributes

REQUIRED_SWEDISH_WORDS = {
    "det",
    "den",
    "vara",
    "är",
    "till",
    "av",
    "och",
    "att",
    "har",
    "med",
}
REQUIRED_DANISH_WORDS = {
    "det",
    "den",
    "være",
    "er",
    "til",
    "af",
    "og",
    "at",
    "har",
    "med",
}
REQUIRED_NORWEGIAN_WORDS = {
    "det",
    "den",
    "være",
    "er",
    "til",
    "av",
    "og",
    "at",
    "har",
    "med",
}


@TaggerRegistry.add("gopher_swedish")
class GopherTaggerSwedish(BaseTagger):
    def predict(self, doc: Document) -> DocResult:
        attrs = get_attributes(doc.text, REQUIRED_WORDS=REQUIRED_SWEDISH_WORDS)
        result = DocResult(doc=doc, spans=attrs.as_spans())
        return result


@TaggerRegistry.add("gopher_danish")
class GopherTaggerDanish(BaseTagger):
    def predict(self, doc: Document) -> DocResult:
        attrs = get_attributes(doc.text, REQUIRED_WORDS=REQUIRED_DANISH_WORDS)
        result = DocResult(doc=doc, spans=attrs.as_spans())
        return result


@TaggerRegistry.add("gopher_norwegian")
class GopherTaggerNorwegian(BaseTagger):
    def predict(self, doc: Document) -> DocResult:
        attrs = get_attributes(doc.text, REQUIRED_WORDS=REQUIRED_NORWEGIAN_WORDS)
        result = DocResult(doc=doc, spans=attrs.as_spans())
        return result
