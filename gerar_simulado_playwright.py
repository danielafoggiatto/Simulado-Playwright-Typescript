
perguntas = [
    {"pergunta": "Qual comando executa a suíte de testes Playwright usando o runner integrado?",
     "alternativas": ["npm test", "npx playwright test", "node playwright run", "playwright run all"],
     "resposta": "b"},

    {"pergunta": "Qual arquivo geralmente contém a configuração do Playwright (projetos, timeouts, reporter)?",
     "alternativas": ["playwright.config.ts", "pwconfig.json", "test.config.js", "config.yml"],
     "resposta": "a"},

    {"pergunta": "Qual é a maneira recomendada de localizar um botão pelo texto visível no Playwright?",
     "alternativas": ["page.locator('button:has-text(\"Salvar\")')","page.querySelector('button:contains(Salvar)')","page.getByText('Salvar')","page.getByRole('button', { name: 'Salvar' })"],
     "resposta": "d"},

    {"pergunta": "Qual método preenche um input de forma que simula digitação com eventos por tecla?",
     "alternativas": ["fill()", "type()", "setValue()", "input()"],
     "resposta": "b"},

    {"pergunta": "O que `test.beforeEach` faz no Playwright Test?",
     "alternativas": ["Executa antes de cada arquivo de teste","Executa antes de cada teste dentro do describe","Executa apenas uma vez antes da suite inteira","Executa após cada teste"],
     "resposta": "b"},

    {"pergunta": "Como criar um contexto de navegador com estado de autenticação salvo?",
     "alternativas": ["browser.newContext({ storageState: 'state.json' })","browser.newPage({ storage: 'state.json' })","browser.launchPersistent('state.json')","page.setStorage('state.json')"],
     "resposta": "a"},

    {"pergunta": "Qual opção de `page.goto()` espera que a rede esteja ociosa antes de retornar?",
     "alternativas": ["{ waitUntil: 'load' }","{ waitUntil: 'networkidle' }","{ waitUntil: 'domcontentloaded' }","{ waitUntil: 'complete' }"],
     "resposta": "b"},

    {"pergunta": "Como você espera que um locator tenha texto específico com timeout personalizado?",
     "alternativas": ["await expect(locator).toHaveText('x', 10000)","await expect(locator).toHaveText('x', { timeout: 10000 })","await expect(locator).toHaveText('x').timeout(10000)","await expect(locator, 10000).toHaveText('x')"],
     "resposta": "b"},

    {"pergunta": "Qual API do Playwright permite interceptar e mockar respostas HTTP?",
     "alternativas": ["page.intercept()", "page.route()", "page.mock()", "page.on('request')"],
     "resposta": "b"},

    {"pergunta": "Como desabilitar o headless para depurar localmente?",
     "alternativas": ["npx playwright test --headed", "npx playwright test --no-headless", "playwright test --headful", "npx playwright open --headful"],
     "resposta": "a"},

    {"pergunta": "Qual é a função de `trace` no Playwright?",
     "alternativas": ["Gravar vídeo da execução", "Registrar rede e ações para visualização em Trace Viewer", "Salvar screenshots apenas", "Executar testes em paralelo"],
     "resposta": "b"},

    {"pergunta": "Como ativar gravação de trace apenas para um teste específico?",
     "alternativas": ["test('x', async ({ page }) => { await page.tracing.start(); ... })", "test.use({ trace: 'on' }) dentro do teste", "test('x', async ({ context }) => { await context.tracing.start({ snapshots: true }); ... })", "Não é possível ativar por teste"],
     "resposta": "c"},

    {"pergunta": "Qual matcher do Playwright valida que um locator está visível?",
     "alternativas": ["toBeShown()", "toBeVisible()", "isVisible()", "toBeDisplayed()"],
     "resposta": "b"},

    {"pergunta": "Como rodar somente testes marcados com @test.skip em Playwright?",
     "alternativas": ["npx playwright test --grep @skip", "npx playwright test --grep \"@skip\"","Não faz sentido","npx playwright test -g skip"],
     "resposta": "c"},

    {"pergunta": "Qual comando gera um relatório HTML padrão do Playwright?",
     "alternativas": ["npx playwright show-report", "npx playwright test --reporter=html", "npx playwright generate-report", "playwright report --html"],
     "resposta": "a"},

    {"pergunta": "Como você seleciona o terceiro elemento usando locator?",
     "alternativas": ["page.locator('div').nth(2)","page.locator('div').nth(3)","page.locator('div')[2]","page.querySelectorAll('div')[2]"],
     "resposta": "a"},

    {"pergunta": "Qual é a forma correta de aguardar que a URL atual contenha um caminho específico?",
     "alternativas": ["await page.waitForURL('/dashboard')","await page.waitForURL(/dashboard/)","await expect(page).toHaveURL('/dashboard')","await expect(page).toHaveURL(/dashboard/)"],
     "resposta": "d"},

    {"pergunta": "O que faz `test.describe.parallel` no Playwright?",
     "alternativas": ["Executa testes dentro do describe em paralelo entre si","Executa cada describe em paralelo com outros describes","Não existe `describe.parallel`","Faz o describe rodar uma única vez"],
     "resposta": "a"},

    {"pergunta": "Qual utilitário é indicado para capturar screenshots quando um teste falha automaticamente?",
     "alternativas": ["configurar em test.use({ screenshot: 'only-on-failure' })","usar page.screenshot() em finally","usar expect.toHaveScreenshot()","não é possível fazer automático"],
     "resposta": "a"},

    {"pergunta": "Como você roda um único teste dentro de um arquivo usando filtro de nome?",
     "alternativas": ["npx playwright test -t 'nome do teste'","npx playwright test --grep 'nome do teste'","npx playwright test --only 'nome'","npx playwright test --filter 'nome'"],
     "resposta": "a"},

    {"pergunta": "Em TypeScript, qual arquivo permite tipagem global para fixtures do Playwright?",
     "alternativas": ["global-setup.ts", "playwright.d.ts", "global.d.ts", "playwright-fixtures.ts"],
     "resposta": "b"},

    {"pergunta": "Como você define tempo máximo de execução por teste no config?",
     "alternativas": ["timeout no test.use", "timeout global em playwright.config.ts -> timeout", "passando timeout na linha de comando", "Não é possível definir globalmente"],
     "resposta": "b"},

    {"pergunta": "Qual comando limpa os traces/gravações locais gerados pelo Playwright?",
     "alternativas": ["npx playwright clean-traces", "rm -rf .playwright/traces || manual", "npx playwright trace clear", "playwright prune traces"],
     "resposta": "b"},

    {"pergunta": "O que `expect.soft` faz em Playwright?",
     "alternativas": ["Faz soft assertion que não falha imediatamente", "Faz assertion que ignora o resultado", "Registro de logs apenas", "Não existe expect.soft"],
     "resposta": "a"},

    {"pergunta": "Como você configura múltiplos projetos (Chrome, Firefox) no Playwright config?",
     "alternativas": ["projects: [{ name: 'chromium', use: { browserName: 'chromium' } }, ...]","browsers: ['chromium','firefox']","setBrowsers(['chromium','firefox'])","Não é suportado"],
     "resposta": "a"},

    {"pergunta": "Para testar comportamentos dependentes de fuso horário, qual opção usar ao criar contexto?",
     "alternativas": ["timezoneId em newContext","setTimezone em page","navigator.timezone em page.evaluate","Não há suporte"], 
     "resposta": "a"},

    {"pergunta": "O que faz `page.route()` quando usado com `route.fulfill()`?",
     "alternativas": ["Intercepta requisição e responde com dado mock", "Bloqueia o request permanentemente", "Redireciona para outra URL", "Faz cache do request"], 
     "resposta": "a"},

    {"pergunta": "Qual das opções é melhor para selecionar elementos por semântica (acessibilidade)?",
     "alternativas": ["page.getByRole()", "page.locator() com seletor CSS", "page.getByText()", "page.querySelector()"], 
     "resposta": "a"},

    {"pergunta": "Como você espera que o número de elementos seja igual a 3?",
     "alternativas": ["expect(locator).toHaveLength(3)", "await expect(locator).toHaveCount(3)", "await expect(locator).toHaveLength(3)", "expect(locator).toHaveCount(3)"], 
     "resposta": "b"},

    {"pergunta": "Qual função permite disparar uma espera customizada baseada em uma condição JS?",
     "alternativas": ["page.waitForFunction()", "page.waitUntil()", "page.pause()", "page.waitForEvent()"], 
     "resposta": "a"},

    {"pergunta": "Como você roda testes em 4 workers no Playwright?",
     "alternativas": ["npx playwright test --workers=4", "npx playwright test -w 4", "npx playwright test --parallel=4", "Não é configurável"], 
     "resposta": "a"},

    {"pergunta": "Qual método do Playwright permite enviar requisições HTTP independentes do browser?",
     "alternativas": ["page.request.get()", "page.fetch()", "page.request.get()", "APIRequestContext via requests em test fixture"], 
     "resposta": "d"},

    {"pergunta": "Quando usar `page.getByLabel()`? ",
     "alternativas": ["Quando o input tiver um <label> associado", "Quando não existir placeholder", "Quando for pesquisar por texto interno", "Quando for elemento sem role"], 
     "resposta": "a"},

    {"pergunta": "Qual API permite gravar um vídeo da execução de um teste?",
     "alternativas": ["page.startVideo()", "context.tracing.start({ screenshots: true })", "usar video: 'on' em test.use/config", "page.recordVideo()"], 
     "resposta": "c"},

    {"pergunta": "Como você remove cookies no contexto antes de cada teste?",
     "alternativas": ["await context.clearCookies()", "await context.clearCookies() não existe", "await context.addCookies([])", "await context.storageState({cookies: []})"], 
     "resposta": "a"},

    {"pergunta": "Qual comando inicia o modo interativo onde você pode depurar passo a passo?",
     "alternativas": ["npx playwright debug", "npx playwright pause", "npx playwright trace view", "npx playwright step"], 
     "resposta": "a"},

    {"pergunta": "Como você marca um teste para ser pulado temporariamente?",
     "alternativas": ["test.skip()", "test.ignore()", "test.xfail()", "test.todo()"], 
     "resposta": "a"},

    {"pergunta": "O que `test.use({ storageState: 'state.json' })` faz em um teste?",
     "alternativas": ["Usa o arquivo de estado para autenticação no contexto", "Salva o estado após o teste", "Substitui playwright.config.ts", "Não existe"], 
     "resposta": "a"},

    {"pergunta": "Qual matcher compara números com tolerância (toBeCloseTo)?",
     "alternativas": ["expect(num).toBeCloseTo(5, 2)", "expect(num).toBeApproximately(5, 2)", "expect(num).toBeNear(5, 2)", "expect(num).toBeClose(5, 2)"], 
     "resposta": "a"},

    {"pergunta": "Como fazer retry automático de testes falhos no Playwright config?",
     "alternativas": ["useRetries: 2", "retries: 2", "testRetries: 2", "retryCount: 2"], 
     "resposta": "b"},

    {"pergunta": "Onde você configura um hook global de setup que roda antes de todos os testes?",
     "alternativas": ["global-setup no playwright.config.ts", "test.beforeAll em cada arquivo", "setup.js na raiz", "package.json"], 
     "resposta": "a"},

    {"pergunta": "Qual é a forma correta de aguardar que um elemento desapareça?",
     "alternativas": ["await expect(locator).toBeHidden()", "await expect(locator).toBeGone()", "await locator.waitFor({ state: 'detached' })", "a e c estão corretas"], 
     "resposta": "d"},

    {"pergunta": "Qual utilitário permite gravar uma trilha de execução (trace) que pode ser visualizada depois?",
     "alternativas": ["traceViewer", "traceViewer não existe", "playwright-trace", "npx playwright show-trace"], 
     "resposta": "d"},

    {"pergunta": "Como evitar que um teste falhe se um expect falhar, mas ainda registrar a falha?",
     "alternativas": ["usar expect.soft", "usar try/catch em every expect", "usar expect(...).catch()", "não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual opção do `page.locator()` melhora a resiliência contra classes dinâmicas?",
     "alternativas": ["usar seletor por data-testid ou getByRole", "usar .className exato", "usar :nth-child", "usar index fixo"], 
     "resposta": "a"},

    {"pergunta": "Como você simula upload de arquivo em um input type=file?",
     "alternativas": ["await page.setInputFiles('input[type=file]', 'caminho')", "await page.uploadFile('input', 'caminho')", "await page.fill('input[type=file]','caminho')", "Não é suportado"], 
     "resposta": "a"},

    {"pergunta": "O que faz `page.pause()` durante um teste?",
     "alternativas": ["Pausa a execução e abre UI de depuração", "Pausa apenas por 1s", "Pausa a execução e fecha o navegador", "Nada"], 
     "resposta": "a"},

    {"pergunta": "Como você pode aguardar a requisição XHR que tem URL parcial '/api/data' antes de prosseguir?",
     "alternativas": ["await page.waitForRequest(req => req.url().includes('/api/data'))","await page.waitForResponse('/api/data')","await page.waitForRequest('/api/data')","Não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual abordagem é recomendada para evitar flakiness em testes?",
     "alternativas": ["usar esperas explícitas aleatórias", "usar seletores estáveis (roles/test-ids) e expect com timeout", "usar sleep grande", "rodar cada teste várias vezes"], 
     "resposta": "b"},

    {"pergunta": "Como você configura para salvar vídeo de todas as execuções em playwright.config.ts?",
     "alternativas": ["use: { video: 'on' }", "video: 'always'", "reporter: ['video']","test.use({ video: 'on' }) global"], 
     "resposta": "a"},

    {"pergunta": "Qual é a maneira correta de chamar um helper TypeScript que exporta funções utilitárias dentro dos testes?",
     "alternativas": ["import { helper } from './helpers/utils'","const helper = require('./helpers/utils')","import helper = require('./helpers/utils')","Usar global"], 
     "resposta": "a"},

    {"pergunta": "O que `expect(locator).toHaveClass(/active/)` checa?",
     "alternativas": ["Que a classe contém o padrão regex", "Que a classe é exatamente 'active'", "Que tem algum filho com classe 'active'", "Que o elemento está ativo no DOM"], 
     "resposta": "a"},

    {"pergunta": "Como você verifica que uma API foi chamada com payload específico via route?",
     "alternativas": ["Intercepcionar com page.route e checar request.postData()", "Não é possível inspecionar", "Usar page.waitForRequest e olhar request.postData()", "a e c são opções válidas"], 
     "resposta": "d"},

    {"pergunta": "Qual comando gera tipagem dos fixtures para TypeScript ao usar Playwright Test?",
     "alternativas": ["npx playwright codegen --types", "npx playwright types generate", "playwright.config.ts cria automaticamente", "npx playwright test --generate-types"], 
     "resposta": "a"},

    {"pergunta": "Qual utilitário permite rodar testes com celular (device emulada)?",
     "alternativas": ["usar em projetos devices['Pixel 5']", "usar page.emulate('mobile')", "rodar em browserstack apenas", "usar mobile: true no locator"], 
     "resposta": "a"},

    {"pergunta": "Como criar um fixture customizado em Playwright Test?",
     "alternativas": ["export const test = base.extend({ myFixture: async ({}, use) => { ... } })","test.createFixture('x')","def fixture():","Não é possível criar fixtures"], 
     "resposta": "a"},

    {"pergunta": "Qual método do locator retorna o texto renderizado visível (sem tags)?",
     "alternativas": ["textContent()", "innerHTML()", "innerText()", "value()"], 
     "resposta": "c"},

    {"pergunta": "Como fazer assert que uma imagem com alt text 'Logo' existe?",
     "alternativas": ["await expect(page.getByAltText('Logo')).toBeVisible()", "await expect(page.getByText('Logo')).toBeVisible()", "await expect(page.locator('img[alt=\"Logo\"]')).toHaveAttribute('alt','Logo')", "a e c"], 
     "resposta": "d"},

    {"pergunta": "Qual recurso ajuda a coletar vídeos, traces e screenshots em execução de CI apenas para falhas?",
     "alternativas": ["configurar retries + artifacts only-on-failure", "usar screenshot: 'on'", "não tem como condicionar", "usar recordOnFailure: true"], 
     "resposta": "a"},

    {"pergunta": "Como você filtra testes por arquivo específico?",
     "alternativas": ["npx playwright test path/to/file.spec.ts", "npx playwright test --file file.spec.ts", "npx playwright test -f file.spec.ts", "npx playwright test --only file"], 
     "resposta": "a"},

    {"pergunta": "Qual prática é recomendada ao escrever seletores para componentes reativos que mudam classes?",
     "alternativas": ["usar data-testid ou getByRole e evitar classes hashadas", "usar classes completas geradas", "usar nth-child fixo", "usar XPath sempre"], 
     "resposta": "a"},

    {"pergunta": "Como você captura network logs via API de request do Playwright (APIRequestContext)?",
     "alternativas": ["const api = await playwright.request.newContext(); await api.get('/url')", "page.request.log()", "page.fetch('/url')", "Não é suportado"], 
     "resposta": "a"},

    {"pergunta": "Qual função do Playwright permite escrever passos nomeados no relatório do trace?",
     "alternativas": ["test.step()", "page.step()", "trace.step()", "trace.log()"], 
     "resposta": "a"},

    {"pergunta": "O que `expect.poll` permite fazer?",
     "alternativas": ["Executar polling até a condição ser verdadeira com timeout", "Fazer assertions suaves sem timeout", "Registrar polling no relatório", "Não existe"], 
     "resposta": "a"},

    {"pergunta": "Como você invalida cache e força reload completo em um teste?",
     "alternativas": ["await page.reload({ force: true })", "await page.reload({ ignoreCache: true })", "await page.reload({ waitUntil: 'networkidle', ignoreCache: true })", "Não é possível ignorar cache"], 
     "resposta": "c"},

    {"pergunta": "Qual é a forma correta de parametrizar testes com dados no Playwright Test?",
     "alternativas": ["usando for ... of dentro de test ou test.describe com test() dinamicamente", "usando pytest parametrize", "usando data-driven plugin", "não é possível parametrizar"], 
     "resposta": "a"},

    {"pergunta": "Como você espera que um locator contenha texto parcial (case-insensitive)?",
     "alternativas": ["await expect(locator).toContainText(/texto/i)", "await expect(locator).toHaveText(/texto/i)", "await expect(locator).toHaveText('texto', { insensitive: true })", "await expect(locator).toContainText('texto', { ignoreCase: true })"], 
     "resposta": "a"},

    {"pergunta": "Qual recurso permite gravar um trace ao falhar e abrir o Trace Viewer posteriormente?",
     "alternativas": ["trace: 'on-first-retry' em config", "trace: 'retry-with-trace'", "usar page.tracing.startOnFail()", "não tem recurso"], 
     "resposta": "a"},

    {"pergunta": "Para rodar testes somente no projeto 'Financeiro' definido no config, qual flag usar?",
     "alternativas": ["--project=Financeiro", "--suite=Financeiro", "--group=Financeiro", "--only=Financeiro"], 
     "resposta": "a"},

    {"pergunta": "Qual é a diferença entre page.locator('text=Salvar') e page.getByText('Salvar')?",
     "alternativas": ["Nenhuma; getByText é helper com validações adicionais","locator('text=') usa engine de texto, getByText usa assertions de acessibilidade","getByText é mais semântico e tem esperas automáticas especializadas","getByText é helper que implementa heurísticas de acessibilidade e fornece mensagens melhores"], 
     "resposta": "d"},

    {"pergunta": "Como você configura testes para rodarem em modo cabeça (headed)?",
     "alternativas": ["npx playwright test --headed", "npx playwright test --no-headless", "npx playwright test --view", "npx playwright test --gui"], 
     "resposta": "a"},

    {"pergunta": "Qual método é mais apropriado para verificar que um toast sumiu da tela?",
     "alternativas": ["await expect(toast).toBeHidden()", "await toast.waitFor({ state: 'hidden' })", "await expect(toast).toBeHidden({ timeout: 5000 })", "Qualquer das anteriores dependendo do caso"], 
     "resposta": "d"},

    {"pergunta": "Como você executa apenas testes marcados com um padrão no nome (grep)?",
     "alternativas": ["npx playwright test --grep 'palavra'","npx playwright test -g 'palavra'","npx playwright test --filter 'palavra'","npx playwright test --name 'palavra'"], 
     "resposta": "a"},

    {"pergunta": "Qual a vantagem de usar fixtures customizadas ao invés de helpers simples?",
     "alternativas": ["Fixtures gerenciam lifecycle e podem ser automaticamente injetadas por teste", "Não há vantagem", "Fixtures são mais lentas", "Helpers têm mais integração com Playwright"], 
     "resposta": "a"},

    {"pergunta": "Como você garante que um teste espere até que os dados do backend sejam atualizados (sem usar sleeps)?",
     "alternativas": ["esperar por um elemento que muda, usar waitForResponse/ waitForRequest ou expect.poll", "esperar um timeout fixo", "usar console.log e verificar manualmente", "usar fetch do navegador"], 
     "resposta": "a"},

    {"pergunta": "Qual é a forma recomendada de organizar Page Objects em TypeScript?",
     "alternativas": ["Cada página em sua classe com métodos que retornam locators e ações", "Uma enorme classe para todo o app", "Funções globais sem classes", "Colocar tudo em fixtures"], 
     "resposta": "a"},

    {"pergunta": "Qual a forma correta de lidar com credenciais sensíveis em CI?",
     "alternativas": ["usar variáveis de ambiente e storageState criptografado no CI", "commitar em arquivo .env no repositório", "colocar no código fonte", "salvar em arquivos públicos"], 
     "resposta": "a"},

    {"pergunta": "Para medir performance (tempo) de uma ação no teste, qual técnica é útil?",
     "alternativas": ["usar console.time e medir no teste", "usar performance.now() via page.evaluate", "medir antes/depois com Date.now() no teste", "usar qualquer das anteriores dependendo do contexto"], 
     "resposta": "d"},

    {"pergunta": "Como você validaria que o texto interno de um card mudou após um filtro sem depender de valores fixos?",
     "alternativas": ["capturar textos antes e depois e comparar se há diferença", "comparar com valor esperado fixo", "checar apenas se existe algum texto", "usar getByText com regex"], 
     "resposta": "a"},

    {"pergunta": "Qual a utilidade de `test.info().attach()` em Playwright Test?",
     "alternativas": ["Anexar artefatos (logs/screenshots) ao relatório do teste", "Enviar email quando teste falha", "Substituir trace", "Salvar variáveis de ambiente"], 
     "resposta": "a"},

    {"pergunta": "Como você ignora temporariamente um teste em TS sem remover o código?",
     "alternativas": ["test.skip()", "test.only()", "marcar xfail", "remover o teste"], 
     "resposta": "a"},

    {"pergunta": "Qual comando cria um snippet inicial (codegen) para reproduzir ações no browser?",
     "alternativas": ["npx playwright codegen <url>", "npx playwright record <url>", "npx playwright capture <url>", "playwright-gen <url>"], 
     "resposta": "a"},

    {"pergunta": "O que `test.only` faz durante a execução da suíte?",
     "alternativas": ["Executa apenas aquele teste marcado como only", "Executa todos exceto o marcado", "Marca o teste como flakey", "Não tem efeito"], 
     "resposta": "a"},

    {"pergunta": "Como você simplifica a escrita de imports/paths com TypeScript em projeto Playwright?",
     "alternativas": ["configurando paths no tsconfig.json", "usando require em vez de import", "colocando tudo em um arquivo index.ts", "não é possível"], 
     "resposta": "a"},

    {"pergunta": "Como aumentar a legibilidade de falhas para debugging em CI?",
     "alternativas": ["Habilitar traces, vídeos e screenshots on failure", "Executar sem reporter", "Desativar retries", "Adicionar muitos prints no teste"], 
     "resposta": "a"},

    {"pergunta": "Qual é a melhor prática ao comparar valores monetários extraídos da UI?",
     "alternativas": ["Normalizar (limpar R$, pontos e vírgulas) e comparar numericamente com tolerância", "Comparar strings exatamente", "Comparar apenas o prefixo 'R$'", "Não comparar valores em testes"], 
     "resposta": "a"},

    {"pergunta": "Como você forçaria o Playwright a esperar até que um elemento esteja clicável (ex: após animação)?",
     "alternativas": ["await expect(locator).toBeEnabled(); await locator.click()", "await page.waitForTimeout(1000); await locator.click()", "await locator.click({ force: true }) sempre", "usar querySelector com setTimeout"], 
     "resposta": "a"},

    {"pergunta": "Como você executa o Playwright Test com um arquivo de configuração diferente?",
     "alternativas": ["npx playwright test --config=outro.config.ts", "npx playwright test -c outro", "npx playwright test --config-file outro", "Não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual é a forma recomendada de verificar atributos dinâmicos (ex: title gerado) em locator?",
     "alternativas": ["await expect(locator).toHaveAttribute('title', /regex/)", "await expect(locator).toHaveText('title')", "ler innerHTML e testar manualmente", "usar snapshot de tela"], 
     "resposta": "a"},

    {"pergunta": "Quando usar page.request em vez de page.route?",
     "alternativas": ["Quando quer chamar API diretamente sem passar pelo browser UI", "Quando quer mockar requisições", "Quando quer interceptar requests de página", "Nunca usar page.request"], 
     "resposta": "a"},

    {"pergunta": "Qual propriedade no config define o número máximo de workers?",
     "alternativas": ["workers", "parallel", "concurrency", "maxWorkers"], 
     "resposta": "a"},

    {"pergunta": "Como você evita testes que dependem da ordem de execução?",
     "alternativas": ["Isolar estado (fixtures) e não depender de testes anteriores", "Executar em série", "Usar nomes em ordem alfabética", "Executar uma vez apenas"], 
     "resposta": "a"},

    {"pergunta": "Qual método do Playwright permite avaliar JS no contexto da página?",
     "alternativas": ["page.evaluate()", "page.exec()", "page.run()", "page.evaluateJs()"], 
     "resposta": "a"},

    {"pergunta": "Como você espera que uma lista tenha ordenação específica após ação?",
     "alternativas": ["Capturar textos da lista antes e depois e comparar a ordem", "Verificar primeiro elemento apenas", "Comparar comprimento apenas", "Usar screenshot diff"], 
     "resposta": "a"},

    {"pergunta": "Qual a vantagem de usar test.step() no roteiro de testes?",
     "alternativas": ["Melhor organização e relatórios mais legíveis em traces", "Faz testes rodarem mais rápido", "Evita retries", "Reduz número de fixtures"], 
     "resposta": "a"},

    {"pergunta": "Como tratar flakiness causado por chamadas assíncronas do backend?",
     "alternativas": ["Usar waitForResponse/expect.poll/esperas por elemento atualizado", "Adicionar sleeps grandes", "Ignorar testes intermitentes", "Sempre usar retries=3"], 
     "resposta": "a"},

    {"pergunta": "Qual forma é mais segura para selecionar um botão que tem texto dinâmico e ícone?",
     "alternativas": ["getByRole('button', { name: /parte do texto/ })", "page.locator('button').nth(0)", "selecionar por classe CSS do ícone", "usar XPath absoluto"], 
     "resposta": "a"},

    {"pergunta": "O que faz `await context.storageState({ path: 'state.json' })`?",
     "alternativas": ["Salva cookies e localStorage no arquivo", "Carrega cookies do arquivo", "Limpa o storage", "Não existe"], 
     "resposta": "a"},

    {"pergunta": "Como você valida que um formulário HTML foi enviado (sem verificar backend)?",
     "alternativas": ["Verificar que houve navegação ou que UI exibiu confirmação", "Verificar apenas console logs", "Esperar 1s e assumir sucesso", "Não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual plugin/integração é comum para visualizar relatórios detalhados de Playwright em CI?",
     "alternativas": ["Playwright HTML Reporter", "Allure Reporter com Playwright adapter", "ReportPortal", "Todas as anteriores dependendo do setup"], 
     "resposta": "d"},

    {"pergunta": "O que usar para simular diferentes geolocalizações no contexto?",
     "alternativas": ["geolocation ao criar context", "page.setGeolocation()", "navigator.geolocation no evaluate", "Não é possível"], 
     "resposta": "a"},

    {"pergunta": "Como você pode armazenar um screenshot diretamente no relatório do teste?",
     "alternativas": ["test.info().attach('screenshot', { body: await page.screenshot(), contentType: 'image/png' })", "console.log page.screenshot()", "salvar em arquivo manual e linkar", "não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual prática impede que selectors quebrados causem falsos positivos?",
     "alternativas": ["Usar selectors semânticos e asserts inteligentes (toBeVisible/toHaveText)", "Usar apenas XPath absoluto", "Ignorar erros de selector", "Usar apenas waits fixos"], 
     "resposta": "a"},

    {"pergunta": "Para que serve page.waitForTimeout e por que usá-lo com cautela?",
     "alternativas": ["Colocar pause fixa; é frágil e deve ser evitado quando possível", "É o método preferido para sincronização", "Substitui espera de rede", "É usado para debug apenas"], 
     "resposta": "a"},

    {"pergunta": "Como você coleta performance trace de uma única ação no Playwright?",
     "alternativas": ["context.tracing.start({ snapshots: true, screenshots: true }); // ação; context.tracing.stop({ path: 'trace.zip' })", "usar page.performance.start()", "usar devtools manualmente", "não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual método permite aguardar múltiplas condições ao mesmo tempo?",
     "alternativas": ["Promise.all com esperas (expect/locator.waitFor)", "awaitAllConditions()", "test.waitMany()", "page.waitForMultiple()"], 
     "resposta": "a"},

    {"pergunta": "Como você configura para que screenshots e vídeos sejam salvos apenas quando um teste falhar?",
     "alternativas": ["usar test.use({ screenshot: 'only-on-failure', video: 'retain-on-failure' }) no config", "usar screenshot: 'on' e filtrar manualmente", "salvar sempre e excluir depois", "Não é possível condicionar"], 
     "resposta": "a"},

    {"pergunta": "O que faz `await page.locator('selector').first().click()`?",
     "alternativas": ["Clica no primeiro elemento que corresponde ao selector", "Clica no último elemento", "Clica em todos os elementos", "Lança erro"], 
     "resposta": "a"},

    {"pergunta": "Como você testa um comportamento que depende de hora do sistema (ex: expiração)?",
     "alternativas": ["mockar Date via page.addInitScript ou ajustar clock no contexto (se suportado)", "mudar o relógio do CI", "usar setTimeout no teste", "não é possível"], 
     "resposta": "a"},

    {"pergunta": "Qual a vantagem de usar `await expect(locator).toHaveText(/regex/)` em vez de assert de igualdade?",
     "alternativas": ["É mais flexível e tolerante a pequenas variações", "É mais rápido", "Evita uso de regex", "Dá mensagens piores"], 
     "resposta": "a"},

    {"pergunta": "Como você injeta um JS antes do carregamento da página (ex: polyfill) em cada teste?",
     "alternativas": ["context.addInitScript()", "page.evaluateOnNewDocument()", "page.addScriptTag()", "a e b são alternativas válidas dependendo do caso"], 
     "resposta": "d"},

    {"pergunta": "Quando usar `locator.getByRole()` em vez de `page.getByRole()`?",
     "alternativas": ["Para buscar dentro de um escopo já localizado", "Não existe `locator.getByRole()`", "Para performance apenas", "Para usar selectors compostos"], 
     "resposta": "a"},

    {"pergunta": "Qual a melhor forma de assegurar que uma mudança UI ocorreu por causa do filtro e não por outro teste?",
     "alternativas": ["Isolar estado no beforeEach e comparar antes/depois no mesmo teste", "Confiar em ordem de execução", "Executar testes em sequência dependente", "Executar em paralelo e confiar no retry"], 
     "resposta": "a"},

    {"pergunta": "O que é recomendado para testes end-to-end confiáveis em CI?",
     "alternativas": ["Ambiente estável, dados fixtures, uso de storageState para autenticação, timeouts ajustados e boa limpeza de artefatos", "Executar todos os testes em paralelo sempre", "Usar headless apenas", "Evitar mocks de API totalmente"], 
     "resposta": "a"},

    {"pergunta": "Qual método permite verificar que checkbox está marcado?",
     "alternativas": ["await expect(locator).toBeChecked()", "await expect(locator).isChecked()", "await expect(locator).checked()", "await expect(locator).toHaveProperty('checked', true)"], 
     "resposta": "a"},

    {"pergunta": "Como capturar console logs da página durante um teste?",
     "alternativas": ["page.on('console', msg => ...)", "console.log na página não é possível", "usar test.info().attach logs", "page.console()"], 
     "resposta": "a"},

    {"pergunta": "Qual opção de `expect` checa que atributo data-qa existe com valor 'x'?",
     "alternativas": ["await expect(locator).toHaveAttribute('data-qa', 'x')", "await expect(locator).toHaveData('qa','x')", "await expect(locator).toHaveProperty('dataset.qa','x')", "await expect(locator).toHaveAttr('data-qa','x')"], 
     "resposta": "a"},

    {"pergunta": "Ao escrever testes em TS, como compilar automaticamente antes de rodar?",
     "alternativas": ["usar ts-node/register ou configurar playwright.config para usar ts-node", "rodar tsc manual", "não precisa compilar", "usar babel"], 
     "resposta": "a"},

    {"pergunta": "Quando usar `await locator.filter({ hasText: 'x' })`?",
     "alternativas": ["Quando precisar filtrar um conjunto de locators por conteúdo interno", "Quando o locator não existir", "Quando quer um CSS mais rápido", "Nunca usar"], 
     "resposta": "a"},

    {"pergunta": "Qual abordagem facilita reuso de selectores complexos entre testes?",
     "alternativas": ["Page Object Model com getters para locators", "Copiar e colar selectors", "Usar variáveis globais no teste", "Escrever selectors inline sempre"], 
     "resposta": "a"},

    {"pergunta": "Como você fecha o contexto e garante limpar estado entre testes?",
     "alternativas": ["await context.close()", "await browser.close()", "await page.close()", "Não fechar contexto"], 
     "resposta": "a"},

    {"pergunta": "Qual comando mostra ajuda das opções do Playwright Test CLI?",
     "alternativas": ["npx playwright test --help", "npx playwright help", "playwright test --options", "playwright --help"], 
     "resposta": "a"},

    {"pergunta": "Por que usar `await expect(locator).toHaveCount(n)` em vez de `await locator.count()` combinado com assert?",
     "alternativas": ["Porque o matcher espera automaticamente até atingir o count", "Porque é mais verboso", "Porque locator.count não funciona", "Não há diferença"], 
     "resposta": "a"},

    {"pergunta": "Como você verifica que um elemento tem estilo CSS display: none?",
     "alternativas": ["await expect(locator).toHaveCSS('display', 'none')", "await expect(locator).toBeHidden()", "Ler style via evaluate e comparar", "a e b dependendo do caso"], 
     "resposta": "d"},

    {"pergunta": "Qual é a vantagem do `APIRequestContext` para testes e2e?",
     "alternativas": ["Permite testar APIs sem abrir browser e integrar com testes de UI", "É mais lento que usar page.request", "Substitui necessidade de UI", "Não é recomendável"], 
     "resposta": "a"},

    {"pergunta": "Como você evita expor dados sensíveis ao postar exemplos de testes (LinkedIn)?",
     "alternativas": ["Anonimizar rotas, nomes de campos e remover tokens antes de postar", "Postar o código direto", "Enviar snapshot do CI", "Colocar credenciais em variáveis no código fonte"], 
     "resposta": "a"},

    {"pergunta": "O que faz `test.slow()` em Playwright?",
     "alternativas": ["Marca o teste como lento e ajusta timeout automaticamente", "Faz o teste rodar devagar", "Ignora o teste", "Não existe"], 
     "resposta": "a"},

    {"pergunta": "Como você valida que um elemento está focado?",
     "alternativas": ["await expect(locator).toBeFocused()", "await expect(locator).toBeActive()", "await locator.isFocused()", "await page.evaluate(() => document.activeElement)"], 
     "resposta": "a"},

    {"pergunta": "Qual técnica é boa para garantir que seu teste local e CI usem states similares?",
     "alternativas": ["Usar storageState exportado e carregar em CI", "Copiar perfil do navegador manualmente", "Ignorar diferença entre ambientes", "Usar dados aleatórios"], 
     "resposta": "a"},

    {"pergunta": "Como você configura retry diferente para CI vs local?",
     "alternativas": ["Definir conditionais no playwright.config.ts dependendo de process.env.CI", "Usar mesmo retry sempre", "Não é possível alterar", "Usar CLI flags apenas"], 
     "resposta": "a"},

     {"pergunta": "Como você configura retry diferente para CI vs local?", 
    "alternativas": ["Definir conditionais no playwright.config.ts dependendo de process.env.CI", "Usar mesmo retry sempre", "Não é possível alterar", "Usar CLI flags apenas"], 
    "resposta": "a"},

    {"pergunta": "Qual é a forma recomendada de gerar vídeos dos testes apenas em falhas durante execução no GitHub Actions?", 
    "alternativas": ["use: { video: 'retain-on-failure' } no playwright.config.ts", "Executar manualmente via CLI", "Definir video: 'on' para todos", "Isso não é possível no CI"], 
    "resposta": "a"},

    {"pergunta": "Como armazenar os relatórios HTML do Playwright como artefato no GitHub Actions?", 
    "alternativas": ["Usando a action upload-artifact após o passo de testes", "Salvando localmente na máquina runner", "Publicando com npm publish", "Gerando PDF manualmente"], 
    "resposta": "a"},

    {"pergunta": "Como garantir que o Playwright use o mesmo navegador instalado no runner do GitHub Actions?", 
    "alternativas": ["Executar npx playwright install --with-deps antes dos testes", "Confiar na instalação global do runner", "Rodar npm rebuild playwright", "Não é necessário em CI"], 
    "resposta": "a"},

    {"pergunta": "O que o comando 'npx playwright test --reporter=github' faz?", 
    "alternativas": ["Gera logs integrados com a interface do GitHub Actions", "Publica relatórios HTML automaticamente", "Executa testes apenas com tags @github", "Desativa os retries"], 
    "resposta": "a"},

    {"pergunta": "Qual prática ajuda a paralelizar testes Playwright em pipelines do GitHub Actions?", 
    "alternativas": ["Dividir specs por matriz de jobs (matrix strategy)", "Rodar tudo num único job", "Usar --workers=1", "Executar manualmente via SSH"], 
    "resposta": "a"},

    {"pergunta": "Como evitar falhas intermitentes no CI causadas por lentidão de rede?", 
    "alternativas": ["Aumentar timeouts no config e usar expect com espera automática", "Desativar espera automática", "Remover todos os waits", "Executar localmente apenas"], 
    "resposta": "a"},

    {"pergunta": "Como integrar testes E2E Playwright com testes unitários no mesmo pipeline?", 
    "alternativas": ["Usando múltiplos jobs, um para unitários e outro para E2E", "Misturando tudo num único arquivo de teste", "Executando Playwright dentro do Jest", "Usando test.describe.parallel"], 
    "resposta": "a"},

    {"pergunta": "Qual variável de ambiente é usada para detectar se o código está rodando no GitHub Actions?", 
    "alternativas": ["process.env.GITHUB_ACTIONS", "process.env.CI_ENV", "process.env.RUNNER", "process.env.IS_PIPELINE"], 
    "resposta": "a"},

    {"pergunta": "Como salvar screenshots automaticamente em falhas dentro do CI?", 
    "alternativas": ["Configurar use: { screenshot: 'only-on-failure' }", "Chamar page.screenshot manualmente", "Ativar modo debug", "Usar CLI com flag --save"], 
    "resposta": "a"},

    {"pergunta": "Como o Playwright distribui os testes quando você usa '--workers=4'?", 
    "alternativas": ["Divide os testes em 4 processos paralelos", "Executa todos no mesmo processo com 4 threads", "Duplica a execução dos testes", "Apenas aumenta o timeout"], 
    "resposta": "a"},

    {"pergunta": "Qual comando permite dividir os testes em múltiplas execuções para paralelizar em diferentes máquinas?", 
    "alternativas": ["--shard=1/3", "--split", "--parallel", "--matrix"], 
    "resposta": "a"},

    {"pergunta": "Quando usar 'test.describe.parallel'?", 
    "alternativas": ["Quando os testes dentro do describe são independentes entre si", "Sempre, para acelerar", "Quando compartilham mesmo estado", "Nunca, pois quebra isolamento"], 
    "resposta": "a"},

    {"pergunta": "Qual é a diferença entre 'test.describe.serial' e 'test.describe.parallel'?", 
    "alternativas": ["Serial executa em sequência, parallel executa simultaneamente", "Parallel é mais lento", "Serial usa threads múltiplas", "Não há diferença prática"], 
    "resposta": "a"},

    {"pergunta": "O que ocorre se dois testes paralelos tentarem modificar o mesmo estado global?", 
    "alternativas": ["Pode gerar falhas imprevisíveis (race conditions)", "Playwright bloqueia automaticamente", "O teste mais rápido vence", "Nada acontece"], 
    "resposta": "a"},

    {"pergunta": "Qual configuração controla o número padrão de workers no Playwright?", 
    "alternativas": ["workers no playwright.config.ts", "threads no package.json", "cpuCount no system", "parallelRuns no CLI"], 
    "resposta": "a"},

    {"pergunta": "Como definir retries específicos apenas para testes flakey?", 
    "alternativas": ["Usando test('nome', { retries: 2 })", "Alterando globalmente no config", "Usando test.retryAll()", "Não é possível definir por teste"], 
    "resposta": "a"},

    {"pergunta": "Por que é recomendado evitar compartilhamento de page entre testes paralelos?", 
    "alternativas": ["Cada teste deve ter isolamento completo do browserContext", "Para reduzir memória", "Porque é mais lento", "Porque o CI falha"], 
    "resposta": "a"},

    {"pergunta": "Qual é o impacto de aumentar 'workers' acima do número de CPUs disponíveis?", 
    "alternativas": ["Pode causar sobrecarga e lentidão geral", "Sempre acelera os testes", "Não afeta desempenho", "Cancela execuções duplicadas"], 
    "resposta": "a"},

    {"pergunta": "Como executar apenas um subconjunto de testes em uma pipeline CI sem alterar o código?", 
    "alternativas": ["Usando tags (@smoke, @critical) e filtros no CLI", "Comentando testes manualmente", "Alterando playwright.config.ts", "Editando node_modules"], 
    "resposta": "a"},

    {"pergunta": "Como o Playwright distribui os testes quando você usa '--workers=4'?", 
    "alternativas": ["Divide os testes em 4 processos paralelos", "Executa todos no mesmo processo com 4 threads", "Duplica a execução dos testes", "Apenas aumenta o timeout"], 
    "resposta": "a"},

    {"pergunta": "Qual comando permite dividir os testes em múltiplas execuções para paralelizar em diferentes máquinas?", 
    "alternativas": ["--shard=1/3", "--split", "--parallel", "--matrix"], 
    "resposta": "a"},

    {"pergunta": "Quando usar 'test.describe.parallel'?", 
    "alternativas": ["Quando os testes dentro do describe são independentes entre si", "Sempre, para acelerar", "Quando compartilham mesmo estado", "Nunca, pois quebra isolamento"], 
    "resposta": "a"},

    {"pergunta": "Qual é a diferença entre 'test.describe.serial' e 'test.describe.parallel'?", 
    "alternativas": ["Serial executa em sequência, parallel executa simultaneamente", "Parallel é mais lento", "Serial usa threads múltiplas", "Não há diferença prática"], 
    "resposta": "a"},

    {"pergunta": "O que ocorre se dois testes paralelos tentarem modificar o mesmo estado global?", 
    "alternativas": ["Pode gerar falhas imprevisíveis (race conditions)", "Playwright bloqueia automaticamente", "O teste mais rápido vence", "Nada acontece"], 
    "resposta": "a"},

    {"pergunta": "Qual configuração controla o número padrão de workers no Playwright?", 
    "alternativas": ["workers no playwright.config.ts", "threads no package.json", "cpuCount no system", "parallelRuns no CLI"], 
    "resposta": "a"},

    {"pergunta": "Como definir retries específicos apenas para testes flakey?", 
    "alternativas": ["Usando test('nome', { retries: 2 })", "Alterando globalmente no config", "Usando test.retryAll()", "Não é possível definir por teste"], 
    "resposta": "a"},

    {"pergunta": "Por que é recomendado evitar compartilhamento de page entre testes paralelos?", 
    "alternativas": ["Cada teste deve ter isolamento completo do browserContext", "Para reduzir memória", "Porque é mais lento", "Porque o CI falha"], 
    "resposta": "a"},

    {"pergunta": "Qual é o impacto de aumentar 'workers' acima do número de CPUs disponíveis?", 
    "alternativas": ["Pode causar sobrecarga e lentidão geral", "Sempre acelera os testes", "Não afeta desempenho", "Cancela execuções duplicadas"], 
    "resposta": "a"},

    {"pergunta": "Como executar apenas um subconjunto de testes em uma pipeline CI sem alterar o código?", 
    "alternativas": ["Usando tags (@smoke, @critical) e filtros no CLI", "Comentando testes manualmente", "Alterando playwright.config.ts", "Editando node_modules"], 
    "resposta": "a"}

]

# HTML template (simples)
html_template_start = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Simulado Playwright + TypeScript - 100 Perguntas</title>
<style>
body { font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }
.pergunta { margin-bottom: 20px; padding: 15px; border: 1px solid #007BFF; /* azul */ border-radius: 8px; background: #ffffff; box-shadow: 0 2px 5px rgba(0, 123, 255, 0.1); }
.resultado { margin-top: 10px; font-weight: bold; }
.correto { color: green; }
.errado { color: red; }
button { margin-top: 10px; padding: 8px 14px; font-size: 15px; font-weight: bold; color: white; background-color: #007BFF; /* azul */ border: none; border-radius: 6px; cursor: pointer; transition: background-color 0.3s ease; } 
button:hover { background-color: #0056b3; /* azul mais escuro */ }
button.check-all { display: block; margin: 20px auto; padding: 10px 20px; font-size: 16px; font-weight: bold; color: white; background-color: #007BFF; /* azul */ border: none; border-radius: 6px; cursor: pointer; transition: background-color 0.3s ease; }
</style>
<script>
function verificar(id, correta) {
    const radios = document.getElementsByName(id);
    let escolhido = null;
    for(const r of radios){ if(r.checked) { escolhido = r.value; break; } }
    const res = document.getElementById("res-" + id);
    if(escolhido === correta) { res.textContent="Correto!"; res.className="resultado correto"; }
    else { res.textContent="Errado! Resposta correta: "+correta; res.className="resultado errado"; }
}
function verificarTodos() {
    const total = document.querySelectorAll('.pergunta').length;
    for(let i=1;i<=total;i++){
        const btn = document.querySelector('#q'+i+' button');
        if(btn) btn.click();
    }
}
</script>
</head>
<body>
<h1>Simulado Playwright + TypeScript - 100 Perguntas</h1>
<p>Dica: responda e use <strong>Verificar</strong> em cada questão. Use <strong>Verificar Todos</strong> para checar tudo de uma vez.</p>
<button class="check-all" onclick="verificarTodos()">Verificar Todos</button>
"""

html_template_end = """
</body>
</html>
"""

# build HTML questions
html_perguntas = ""
for i, p in enumerate(perguntas, 1):
    html_perguntas += f'<div class="pergunta" id="q{i}">\n'
    html_perguntas += f'<p><strong>{i}. {p["pergunta"]}</strong></p>\n'
    for j, alt in zip(["a","b","c","d"], p["alternativas"]):
        html_perguntas += f'<label><input type="radio" name="q{i}" value="{j}"> {alt}</label><br>\n'
    html_perguntas += f'<button onclick="verificar(\'q{i}\',\'{p["resposta"]}\')">Verificar</button>\n'
    html_perguntas += f'<div class="resultado" id="res-q{i}"></div>\n</div>\n\n'

with open("simulado_playwright.html", "w", encoding="utf-8") as f:
    f.write(html_template_start + html_perguntas + html_template_end)

print("Arquivo simulado_playwright.html gerado com sucesso! Abra no navegador para visualizar.")
