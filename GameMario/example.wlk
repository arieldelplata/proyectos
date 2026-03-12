import wollok.game.*

object juego {

  const backgroundSound = game.sound("musicaFondo.mp3")

  method iniciar(){
    game.width(30)
    game.height(12)
    game.boardGround("Grass_Sample.jpg")
    game.addVisualCharacter(mario)

    game.onCollideDo(mario,{algo=> algo.teAgarroMario()})

    game.onTick(5000,"generar goomba",{self.generarGoombas()})
    game.onTick(10000,"generar moneda",{self.generarMonedas()})
    game.onTick(15000,"generar hongo",{self.generarHongos()})
    backgroundSound.volume(0.1)
    backgroundSound.shouldLoop(true)
    game.schedule(500, {backgroundSound.play()})

    game.start()
    
  }
    method generarGoombas(){
      const pos = self.posicionAleatoria()
      new Goomba(position = pos).aparecer()
    }
  
  method generarHongos(){
    const pos = self.posicionAleatoria()
    new Hongos(position = pos).aparecer()
  }
  method generarMonedas(){
    const pos = self.posicionAleatoria()
    new Monedas(position = pos).aparecer()
  }

  method posicionAleatoria() = game.at(
    0.randomUpTo(game.width()),
    0.randomUpTo(game.height())
  )

}

object mario{
  var imagenActual = "Mario.png"
  var property soyInmortal = false 
  var property position = game.center()
  var property puntos = 0
  var property vida = 100

  var property image1 = "Mario.png"
  var property image2 = "SuperMario.png"
  
  method cambiarImagen(nuevaImagen){
    imagenActual = nuevaImagen
    game.hasVisual(imagenActual)
  }

  method decirVida(){
    return vida
  }

  method decirPuntos(){
    return puntos
  }

  method inmortal(){
    soyInmortal = true
    return
  }

  method aumentarVida(){
    vida = 100
  }

  method aumentarPuntos(){
    puntos += 1
  }

  method perderVida(){
    vida = vida - 10
  }
  
}

class Goomba{
  var property position
  method image()  = "Goomba.png"
  
  method aparecer(){
    game.addVisual(self)
  }

  method teAgarroMario(){
    if (mario.soyInmortal()){
      game.removeVisual(self)}
    else {
      mario.perderVida()
      game.say(mario,"mi vida es " + mario.decirVida())
      game.removeVisual(self)}

      //si mario es inmortal que lo pueda comer sin recibir daño, pero por lo contrario que le reste vida y muestre su vida, y eliminarse
    }

  

}

class Hongos{
  var property position
  method image()  = "Super Mushroom.png"

  method aparecer(){
    game.addVisual(self)
  }

  method teAgarroMario(){
    mario.cambiarImagen(mario.image2) //no esta cambiando la imagen
    mario.aumentarVida() 
    mario.inmortal()
    game.say(mario,"soy inmortal")
    game.onTick(10000,"mario ya no es inmortal",mario.inmortal())
    game.onTick(10000,"mario ya no es inmortal",game.say(mario,"soy inmortal"))
    game.removeVisual(self)
    //cambiar al sprite de mario grande por x segundos y hacerlo inmortal ese mismo tiempo, restaurar vida y eliminarse 
  }

  

}

class Monedas{
  var property position
  const property valor = 100
  method image()  = "Coin.png"

  method aparecer(){
    game.addVisual(self)
  }

  method teAgarroMario(){
    mario.aumentarPuntos()
    game.removeVisual(self)
    game.say(mario,"tengo " + mario.puntos() + " puntos")
    game.removeTickEvent(self)
    //aumentar puntos de mario, decir cuantos puntos tiene mario y eliminarse
  }

  
}