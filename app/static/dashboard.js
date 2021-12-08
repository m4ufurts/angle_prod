let google_carregado = false;
let calibragens = [];
let calibracao_atual = null;

google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(() => { 
  google_carregado = true;
  atualizar_grafico();
});


$( document ).ready(async ()=>{
  carregar_calibracao();
  carregar_registro();
});

async function carregar_calibracao(){
  calibragens = await $.get("/dashboard/calibracao");

  calibragens.forEach( e => {
    $('#select_calibration').append(`<option value="${e.id}">${e.produto__tipo}</option>`)
  })

  if(calibragens.length >= 1){
    selecionar_calibracao(calibragens[0].id)
  }
}

async function carregar_registro(){
  registros = await $.get("/dashboard/registro");

  registros.forEach( e => {
    $('tbody').append(
      `<tr>
          <td>${e.descricao}</td>
          <td>${e.categoria__nome}</td>
          <td>${e.fornecedor__nome}</td>
          <td>${ parseInt(100 * (e.ganho_anual- e.custo_esperado)/e.ganho_anual) / 100 }</td>
      </tr>`
      )
  })

  const { ganho_anual, angle_anual} = await $.get("/dashboard/registro_resumo");
  $("#angle_anual").html(`R$ ${parseInt( angle_anual * 100 ) / 100}`);
  $("#ganho_anual").html(`R$ ${parseInt( ganho_anual * 100 ) / 100}`);

  atualizar_grafico();
}

async function atualizar_calibracao(e, prop){
  const calibracao = calibragens.find( c => c.id == calibracao_atual);
  calibracao[prop] = parseInt(e.target?.value) / 100;

  await $.post(`/dashboard/calibracao/${calibracao.id}`, calibracao);

  selecionar_calibracao(calibracao_atual)
}

function selecionar_calibracao(e){
  calibracao_atual = e.target?.value || e;
  const calibracao = calibragens.find( c => c.id == calibracao_atual);
  
  $('#materia_prima .value').html(`${parseInt(100 * calibracao.materia_prima)}%`);
  $('#materia_prima input').prop('value', 100 * calibracao.materia_prima); 


  $('#processo .value').html(`${parseInt(100 * calibracao.processo)}%`);
  $('#processo input').prop('value', 100 * calibracao.processo); 

  $('#produtividade .value').html(`${parseInt(100 * calibracao.produtividade)}%`);
  $('#produtividade input').prop('value',100 *  calibracao.produtividade); 

  $('#markup .value').html(`${parseInt(100 * calibracao.markup)}%`);
  $('#markup input').prop('value', 100 * calibracao.markup); 
}

function atualizar_grafico() {
  if(!google_carregado) return;

  const dados = registros.map( e => [ e.ganho_anual, e.angle_anual ]);

  var data = google.visualization.arrayToDataTable([
    ['Angle', 'Custo'],
    ...dados
  ]);

  var options = {
    title: 'Angle vs. Custo',
    hAxis: {title: 'Angle', minValue: 0, maxValue: 50},
    vAxis: {title: 'Custo', minValue: 0, maxValue: 50},
    legend: 'none'
  };

  var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));

  chart.draw(data, options);
}